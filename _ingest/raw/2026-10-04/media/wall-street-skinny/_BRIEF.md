# Analyst brief — Wall Street Skinny concept notes

You are writing ONE course-grade teaching note for **The Compounding MBA** (`/Users/kalvaryhawkins/self-mba`),
distilled from The Wall Street Skinny YouTube channel (hosts: Kristen Kelly, ex-Morgan Stanley IBD, and
Jen Saarbach, ex-Morgan Stanley S&T; plus guests). Transcripts are in this folder; your cluster's file list
is in `_clusters.json` under your cluster key. Read ALL of them (long videos fully; skim recaps/banter).

## What the user wants
They want to *understand the concepts*, not get a video summary. For every important concept the
channel teaches, answer: what is it, how does it work, why does it matter to a business, what forces
drive it, and what the world looks like with vs. without it.

## Output
Write `notes/wss-<cluster-key>.md`. Structure:

1. Header blockquote: sources (count of videos/shorts used, raw path `_ingest/raw/2026-10-04/media/wall-street-skinny/`),
   which courses it maps to (see CURRICULUM.md: Courses 01–12, Exec E1–E12), and a ⚠ bias line (hosts are
   ex-sell-side, guests are often selling their asset class; flag where this shows).
2. **"What this adds to the program"**: 3–5 bullets. First check what already exists: grep `notes/`, `learn/`,
   `GLOSSARY.md`, `notes/canon/` for the concept. Don't re-teach what the repo already covers well; link to it
   and add only the new angle.
3. **Concept map**: a short table — concept | one-line definition | why it matters | already in repo? (y/partial/n)
4. **One section per concept** (aim for 8–15 concepts, ordered foundational → advanced), each with exactly:
   - **What it is**: plain language, 2–3 sentences, no jargon left undefined
   - **How it works**: mechanics, with the actual numbers/deals the hosts used (show the arithmetic)
   - **Business significance / value**: who uses it, where value is created or captured, who pays
   - **Forces & impact**: what drives it (rates, regulation, incentives, cycles) and its second-order effects
   - **With vs. without**: the counterfactual. What happens if this mechanism didn't exist, or when it breaks
   - **Applies when / Breaks when**
   - **Channel example**: the specific deal/event and the video title it came from
   - **Counterpoint**: where the hosts/guest are one-sided, or where reality disagrees
   - **Links**: `[[existing-note]]` / `[[canon-...]]` cross-links (only to files that actually exist; check)
5. **How the concepts connect**: a short paragraph or ASCII chain showing causal links between concepts
   (e.g. rates ↑ → floating-rate borrowers squeezed → PIK toggles → private credit marks lag → gating).
6. **Retrieval questions**: 8–12 questions that test understanding (not recall), with short answers.
7. **Gaps**: concepts the channel covers in videos whose transcripts are missing (see catalog JSONs
   `/Users/kalvaryhawkins/wss_all_videos.json` and `wss_all_shorts.json` vs. files present). List titles to fold in later.

## Rules
- Write in your own words. At most a few brief attributed quotes (under 15 words each). Never reproduce transcript passages.
- Match the voice of existing notes, e.g. `notes/trading-floor-mechanics.md` and `notes/tiger-sisters-insights.md`
  (read one first). Dense, specific, no filler, no emoji.
- Numbers: use the figures said in the video and attribute them; if a figure looks wrong or dated, say so.
- Do NOT edit any file other than your own note. Return a 5-line summary: concepts covered, biggest
  new insight, gaps.
