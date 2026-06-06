#!/usr/bin/env python3
"""
Bulk-pull runner for the Compounding MBA.

Reads manifest.json and, per module, fetches:
  - YouTube transcripts (via the `research` CLI -> yt-dlp), scored
  - Reddit threads (via the `research` CLI), scored
  - SEC EDGAR overview + facts (via edgar.py)

Writes JSON/text into _ingest/raw/<date>/<track>/<module>/ and logs progress.
Designed to run unattended (launchd-friendly): absolute paths, per-item error
isolation, polite pacing. One broken source never aborts the run.

Usage:
  python3 pull.py                     # full pull, all modules
  python3 pull.py --only 01-accounting
  python3 pull.py --track core        # core or exec
  python3 pull.py --n-yt 5 --n-reddit 30 --no-transcripts
"""
import argparse, json, os, subprocess, sys, time
from datetime import date

HOME = os.path.expanduser("~")
SELF_MBA = os.path.join(HOME, "self-mba")
INGEST = os.path.join(SELF_MBA, "_ingest")
RESEARCH = os.path.join(HOME, "research-kit", ".venv", "bin", "research")
EDGAR = os.path.join(INGEST, "edgar.py")
EDGAR_UA = os.environ.get("EDGAR_UA", "Compounding-MBA techforge8yte@gmail.com")

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", file=sys.stderr, flush=True)

def slug(s):
    return "".join(c if c.isalnum() else "-" for c in s.lower())[:60].strip("-")

def run(cmd, outfile=None, env=None, timeout=600):
    """Run a subprocess; capture stdout to outfile if given. Returns ok:bool."""
    try:
        e = dict(os.environ, **(env or {}))
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=e)
        if outfile and r.stdout.strip():
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(r.stdout)
        if r.returncode != 0:
            log(f"    ! exit {r.returncode}: {(r.stderr or '').strip()[:160]}")
            return False
        return True
    except subprocess.TimeoutExpired:
        log(f"    ! timeout after {timeout}s")
        return False
    except Exception as ex:
        log(f"    ! {ex}")
        return False

def pull_module(track, name, spec, outdir, n_yt, n_reddit, transcripts):
    mdir = os.path.join(outdir, track, name)
    os.makedirs(mdir, exist_ok=True)
    counts = {"yt": 0, "reddit": 0, "edgar": 0}

    for q in spec.get("yt", []):
        out = os.path.join(mdir, f"yt_{slug(q)}.json")
        cmd = [RESEARCH, "yt", q, "-n", str(n_yt), "--score"]
        if transcripts:
            cmd.append("--transcripts")
        log(f"    yt: {q!r}")
        if run(cmd, outfile=out, timeout=900):
            counts["yt"] += 1
        time.sleep(1.5)  # be polite to YouTube

    for rd in spec.get("reddit", []):
        sub = rd.get("sub", "")
        q = rd.get("q")
        label = f"{sub}{'_' + slug(q) if q else ''}"
        out = os.path.join(mdir, f"reddit_{label}.json")
        if q:
            cmd = [RESEARCH, "reddit", q, "--sub", sub, "-n", str(n_reddit), "--score"]
        else:
            cmd = [RESEARCH, "reddit", "--sub", sub, "--listing", "top", "--time", "year", "-n", str(n_reddit), "--score"]
        log(f"    reddit: r/{sub}{' q=' + q if q else ''}")
        if run(cmd, outfile=out, timeout=300):
            counts["reddit"] += 1
        time.sleep(1.0)

    for tk in spec.get("tickers", []):
        out = os.path.join(mdir, f"edgar_{slug(tk)}.txt")
        log(f"    edgar: {tk}")
        if run(["python3", EDGAR, "company", tk], outfile=out,
               env={"EDGAR_UA": EDGAR_UA}, timeout=180):
            counts["edgar"] += 1
        time.sleep(0.5)

    log(f"  done {track}/{name}: {counts['yt']} yt, {counts['reddit']} reddit, {counts['edgar']} edgar")
    return counts

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--only", help="single module name, e.g. 01-accounting")
    p.add_argument("--track", choices=["core", "exec", "canon"], help="limit to one track")
    p.add_argument("--n-yt", type=int, default=5)
    p.add_argument("--n-reddit", type=int, default=25)
    p.add_argument("--no-transcripts", action="store_true")
    args = p.parse_args()

    with open(os.path.join(INGEST, "manifest.json")) as f:
        manifest = json.load(f)

    today = date.today().isoformat()
    outdir = os.path.join(INGEST, "raw", today)
    os.makedirs(outdir, exist_ok=True)

    tracks = [args.track] if args.track else ["core", "exec"]
    total = {"yt": 0, "reddit": 0, "edgar": 0}
    t0 = time.time()
    log(f"=== bulk pull start -> {outdir} ===")
    for track in tracks:
        for name, spec in manifest.get(track, {}).items():
            if name.startswith("_"):
                continue
            if args.only and name != args.only:
                continue
            log(f"[{track}] {name}")
            c = pull_module(track, name, spec, outdir, args.n_yt, args.n_reddit,
                            not args.no_transcripts)
            for k in total:
                total[k] += c[k]

    dt = time.time() - t0
    log(f"=== DONE in {dt/60:.1f} min — {total['yt']} yt files, "
        f"{total['reddit']} reddit files, {total['edgar']} edgar files ===")
    # write a manifest of what landed
    summary = {"date": today, "elapsed_min": round(dt / 60, 1), "totals": total,
               "outdir": outdir}
    with open(os.path.join(outdir, "_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

if __name__ == "__main__":
    main()
