"""Extract research results from agent output JSONL files and save as markdown."""
import json, os, re

TASKS_DIR = "/private/tmp/claude-501/-Users-kalvaryhawkins/17552c91-de13-4802-8dbf-b0c7e83f3213/tasks"
OUT_DIR = os.path.expanduser("~/self-mba/quant-backtesting/research")
os.makedirs(OUT_DIR, exist_ok=True)

TOPIC_MAP = {
    "a0b22925e6b2f1baa": "harvey-liu-zhu-backtesting-pitfalls",
    "a1c327919defb8da7": "robert-carver-systematic-trading",
    "a25e18959897f6290": "citadel",
    "a260a94d2f25e0679": "academic-frameworks-multiple-testing",
    "a2bf15a69df07cc30": "de-shaw",
    "a359c6a4dfd47f1d6": "youtube-watchlist-research",
    "a48f363345db3483c": "two-sigma",
    "a4eaefcb86169109f": "ernest-chan",
    "a6830f2b89ba8e022": "main-compilation",
    "a6914a1babda8bfb7": "bridgewater",
    "a6e021f512a040e6e": "renaissance-technologies",
    "a8850b3509aadbc0f": "lopez-de-prado",
    "a96ab7f677e180d86": "youtube-podcasts-search",
    "a9e880b8eeb0f5a4a": "self-mba-audit",
    "aa64e071c091ba3ac": "factor-models-regime-detection",
    "ab7b8c43a7b785b78": "backtesting-architecture",
    "abb53c06c89f7f70c": "bloomberg-tradeweb",
    "acbe90051731094f7": "youtube-channels-search",
    "aff6dc07c55bcdd2b": "aqr-capital",
}

for fname in sorted(os.listdir(TASKS_DIR)):
    if not fname.endswith(".output"):
        continue
    task_id = fname.replace(".output", "")
    slug = TOPIC_MAP.get(task_id)
    if not slug:
        continue

    filepath = os.path.join(TASKS_DIR, fname)
    last_text = None
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("type") == "assistant":
                msg = obj.get("message", {})
                content = msg.get("content", "")
                if isinstance(content, list):
                    text_parts = [b.get("text", "") for b in content if b.get("type") == "text"]
                    content = "\n".join(text_parts)
                if content and len(content) > 200:
                    last_text = content

    if last_text:
        out_path = os.path.join(OUT_DIR, f"{slug}.md")
        with open(out_path, "w") as f:
            f.write(last_text)
        print(f"OK  {slug}.md ({len(last_text)} chars)")
    else:
        print(f"SKIP {slug} (no substantial content found)")
