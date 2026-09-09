"""Fetch YouTube transcripts for the quant backtesting watchlist."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/research-kit"))

from research_kit.youtube import transcript

VIDEOS = {
    "PHe0bXAIuk0": "Ray Dalio - How The Economic Machine Works",
    "QxhxLwNbMMg": "Lopez de Prado - Dangers of Backtest Overfitting",
    "lhCL4R3JFOc": "Cliff Asness AQR on Bloomberg Money Stuff",
    "T-W0OzzoMKM": "How Overfit Is Your Backtest - Lopez de Prado PBO",
    "FJYgrkVbpEE": "Advances in Financial ML - de Prado Interview",
    "X72PZ_tQ4cA": "Jim Simons - Quant Trading and Data Science",
    "_5JkBUeLOLQ": "Greg Zuckerman on Jim Simons and RenTech",
    "klwnw3iSRuM": "Robert Carver - Simplicity in Systematic Trading",
    "DW9zQ8Hz6gQ": "Chat with Traders x Ernie Chan - How Quant Strategies Are Developed",
    "xPsxHlyz098": "Ernest Chan - Truth About Algorithmic Trading",
    "QNznD9hMEh0": "Jim Simons - Numberphile Full Interview",
}

OUT_DIR = os.path.expanduser("~/self-mba/quant-backtesting/transcripts")
SUBS_DIR = os.path.join(OUT_DIR, ".cache")
os.makedirs(SUBS_DIR, exist_ok=True)

for vid, title in VIDEOS.items():
    slug = title.lower().replace(" ", "-").replace("'", "")
    slug = "".join(c for c in slug if c.isalnum() or c == "-")[:80]
    out_path = os.path.join(OUT_DIR, f"{slug}.txt")
    if os.path.exists(out_path):
        print(f"SKIP  {title}")
        continue
    print(f"FETCH {title} ({vid})...", end=" ", flush=True)
    text = transcript(vid, subs_dir=SUBS_DIR, cookies_browser="chrome", timeout=240)
    if text:
        with open(out_path, "w") as f:
            f.write(f"# {title}\n")
            f.write(f"# https://www.youtube.com/watch?v={vid}\n\n")
            f.write(text)
        print(f"OK ({len(text)} chars)")
    else:
        print("FAILED (no captions)")

print("\nDone.")
