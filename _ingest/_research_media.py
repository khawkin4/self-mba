#!/usr/bin/env python3
"""Research new practitioner/media veins — pull YouTube transcripts into
raw/2026-06-05/media/<vein>/ for synthesis into reference notes.
(Articles/books handled separately as cited summaries — NOT scraped here.)
Run:  python3 _ingest/_research_media.py
"""
import os, subprocess, sys, time
HOME = os.path.expanduser("~")
RESEARCH = os.path.join(HOME, "research-kit", ".venv", "bin", "research")
OUT = os.path.join(HOME, "self-mba", "_ingest", "raw", "2026-06-05", "media")

VEINS = {
    "earn-your-leisure": [
        "Earn Your Leisure business breakdown wealth", "Market Mondays investing advice",
        "Earn Your Leisure financial literacy ownership", "Earn Your Leisure how to build wealth"],
    "athletes-investing": [
        "why professional athletes go broke financial lessons", "athletes investing venture capital building wealth",
        "athlete entrepreneur business empire", "athlete financial advice money management"],
    "hbr-ideacast": [
        "HBR IdeaCast strategy interview", "Harvard Business Review leadership podcast",
        "HBR on management decision making"],
    "forbes": [
        "Forbes billionaire business strategy interview", "Forbes how I built this entrepreneur",
        "Forbes investing wealth building"],
    "harlem-capital": [
        "Henri Pierre-Jacques Harlem Capital venture capital", "Harlem Capital how VC works term sheet",
        "Brandon Bryant Harlem Capital diverse founders", "Henri Pierre-Jacques how to raise venture capital",
        "Harlem Capital fund strategy investing in startups", "how venture capital funds make money carry"],
}

def slug(s): return "".join(c if c.isalnum() else "-" for c in s.lower())[:60].strip("-")

def run(cmd, out, timeout=900):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if r.stdout.strip(): open(out, "w", encoding="utf-8").write(r.stdout); return True
        sys.stderr.write(f"   ! empty: {' '.join(cmd[-2:])}\n")
    except Exception as ex: sys.stderr.write(f"   ! {ex}\n")
    return False

def main():
    only = set(sys.argv[1:])  # optional: restrict to named veins
    ok = 0
    for vein, qs in VEINS.items():
        if only and vein not in only: continue
        d = os.path.join(OUT, vein); os.makedirs(d, exist_ok=True)
        for q in qs:
            sys.stderr.write(f"[{vein}] {q!r}\n")
            if run([RESEARCH, "yt", q, "-n", "3", "--score", "--transcripts"],
                   os.path.join(d, f"yt_{slug(q)}.json")): ok += 1
            time.sleep(1.5)
    print(f"DONE: {ok} yt files across {len(VEINS)} veins", file=sys.stderr)

if __name__ == "__main__":
    main()
