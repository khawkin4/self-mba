#!/usr/bin/env python3
"""Targeted re-pull: fetch book-SPECIFIC YouTube transcripts for the 33 corpus-thin
canon notes, written into the EXISTING raw/2026-06-05/canon/<cluster>/ folders
(new filenames yt_fix_<book>.json — never clobbers the originals).

Run:  python3 _ingest/_repull_thin.py
Then re-run the enrichment workflow on just the thin notes.
"""
import glob, json, os, re, subprocess, sys, time

HOME = os.path.expanduser("~")
RESEARCH = os.path.join(HOME, "research-kit", ".venv", "bin", "research")
ROOT = os.path.join(HOME, "self-mba")
NOTES = os.path.join(ROOT, "notes", "canon")
CANON_RAW = os.path.join(ROOT, "_ingest", "raw", "2026-06-05", "canon")

NAME2SLUG = {
    "Strategy": "strategy", "Leadership & Presence": "leadership-presence",
    "Mental Models & Thinking": "mental-models", "Org Design & Mechanisms": "org-design-mechanisms",
    "Landscape & Competitive Awareness": "landscape-competitive", "Negotiation & Influence": "negotiation-influence",
    "Execution & Operations": "execution-operations", "Culture & Change": "culture-change",
    "Risk, Uncertainty & Fragility": "risk-fragility", "Product Thinking & Innovation": "product-innovation",
    "Power & Organizational Politics": "power-politics", "Personal Effectiveness": "personal-effectiveness",
    "Financial Literacy for Operators": "financial-literacy", "Behavioral Design & Decision Science": "behavioral-decision",
    "Game Theory & Strategic Interaction": "game-theory", "Network Effects & Platform Strategy": "platform-strategy",
    "Systems Thinking & Complexity": "systems-complexity", "Information & Communication": "information-communication",
    "Economics & Incentive Design": "economics-incentives", "History & Judgment": "history-judgment",
    "Communication & Storytelling": "communication-storytelling", "Design Thinking & Problem-Solving": "design-problem-solving",
    "Ethics & Judgment": "ethics-judgment",
}

# Hand-crafted book-specific queries for stronger transcripts (fallback = derived from slug).
QUERY = {
    "canon-ariely-predictably-irrational": "Dan Ariely Predictably Irrational book summary decoy effect",
    "canon-akerlof-market-for-lemons": "Akerlof market for lemons adverse selection explained",
    "canon-allison-essence-of-decision": "Graham Allison Essence of Decision rational actor organizational politics",
    "canon-badaracco-defining-moments": "Joseph Badaracco Defining Moments right versus right ethics",
    "canon-bungay-art-of-action": "Stephen Bungay Art of Action directed opportunism mission command",
    "canon-christensen-innovators-dilemma": "Clayton Christensen Innovators Dilemma disruptive innovation explained",
    "canon-clausewitz-on-war": "Clausewitz On War friction fog of war culminating point",
    "canon-cialdini-pre-suasion": "Robert Cialdini Pre-Suasion summary attention",
    "canon-covey-7-habits": "Stephen Covey 7 Habits of Highly Effective People summary",
    "canon-cusumano-business-of-platforms": "Business of Platforms innovation transaction platform strategy",
    "canon-goldratt-the-goal": "Goldratt The Goal theory of constraints bottleneck summary",
    "canon-greene-48-laws-of-power": "48 Laws of Power Robert Greene summary",
    "canon-grove-only-the-paranoid-survive": "Andy Grove Only the Paranoid Survive strategic inflection point",
    "canon-hagiu-wright-multi-sided-platforms": "multi-sided platform pricing subsidize side network effects",
    "canon-kahneman-thinking-fast-and-slow": "Thinking Fast and Slow Kahneman system 1 system 2 summary",
    "canon-kahneman-sibony-sunstein-noise": "Kahneman Noise a flaw in human judgment summary",
    "canon-klein-sources-of-power": "Gary Klein recognition primed decision making naturalistic",
    "canon-march-primer-decision-making": "James March garbage can model organizational decision making",
    "canon-mauboussin-success-equation": "Michael Mauboussin Success Equation skill versus luck",
    "canon-meadows-leverage-points": "Donella Meadows twelve leverage points to intervene in a system",
    "canon-munger-poor-charlies-almanack": "Charlie Munger psychology of human misjudgment mental models",
    "canon-neustadt-may-thinking-in-time": "Neustadt May Thinking in Time historical analogies decision makers",
    "canon-parker-platform-revolution": "Platform Revolution network effects core interaction cold start",
    "canon-parrish-great-mental-models": "Shane Parrish Great Mental Models Farnam Street circle of competence",
    "canon-patterson-crucial-conversations": "Crucial Conversations silence violence mutual purpose summary",
    "canon-perrow-normal-accidents": "Charles Perrow Normal Accidents tight coupling complexity",
    "canon-pfeffer-power": "Jeffrey Pfeffer Power why some people have it Stanford",
    "canon-rumelt-the-crux": "Richard Rumelt The Crux how to solve hardest part of any challenge",
    "canon-shannon-information-theory": "Claude Shannon information theory entropy explained",
    "canon-shapiro-varian-information-rules": "Information Rules Shapiro Varian lock-in switching costs versioning",
    "canon-stone-difficult-conversations": "Difficult Conversations three conversations what happened feelings identity",
    "canon-taleb-black-swan": "Nassim Taleb Black Swan summary fat tails",
    "canon-taleb-antifragile": "Nassim Taleb Antifragile barbell optionality summary",
    "canon-tetlock-superforecasting": "Philip Tetlock Superforecasting ten commandments calibration",
    "canon-thaler-sunstein-nudge": "Thaler Sunstein Nudge choice architecture defaults summary",
    "canon-thucydides-peloponnesian-war": "Thucydides Peloponnesian War Melian dialogue Thucydides trap",
    "canon-tufte-visual-display": "Edward Tufte visual display quantitative information data-ink chartjunk",
}

def cluster_of(note_path):
    txt = open(note_path, encoding="utf-8").read()
    m = re.search(r"Cluster:\s*(.+?)\s*·", txt)
    return NAME2SLUG.get(m.group(1).strip()) if m else None

def run(cmd, outfile, timeout=900):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        if r.stdout.strip():
            open(outfile, "w", encoding="utf-8").write(r.stdout)
            return True
        sys.stderr.write(f"   ! empty: {' '.join(cmd[-3:])}\n")
    except Exception as ex:
        sys.stderr.write(f"   ! {ex}\n")
    return False

def main():
    thin = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(NOTES, "canon-*.md"))
                  if "corpus thin" in open(p, encoding="utf-8").read())
    print(f"thin notes: {len(thin)}", file=sys.stderr)
    ok = 0
    for book in thin:
        cl = cluster_of(os.path.join(NOTES, book + ".md"))
        if not cl:
            sys.stderr.write(f"   ! no cluster for {book}\n"); continue
        d = os.path.join(CANON_RAW, cl); os.makedirs(d, exist_ok=True)
        q = QUERY.get(book, book.replace("canon-", "").replace("-", " ") + " book summary")
        out = os.path.join(d, f"yt_fix_{book.replace('canon-', '')}.json")
        sys.stderr.write(f"[{cl}] {book}: {q!r}\n")
        if run([RESEARCH, "yt", q, "-n", "2", "--score", "--transcripts"], out):
            ok += 1
        time.sleep(1.5)
    print(f"DONE: {ok}/{len(thin)} re-pulled", file=sys.stderr)

if __name__ == "__main__":
    main()
