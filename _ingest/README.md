# Ingestion Pipeline

Turns the curriculum into a repeatable weekly pull. Three source engines feed one
distilled-notes folder (`~/self-mba/notes/`):

```
  research skill ──┐
  (YouTube + Reddit)│
                    ├──►  distill (deep-research)  ──►  ~/self-mba/notes/<course>/*.md
  edgar.py ─────────┘
  (SEC filings + data)
```

## The two engines

**1. `research` skill** — lectures, founder talks, and practitioner threads.
Invoke `/research` (or the `research` skill) per course with the channels/subreddits from
`CURRICULUM.md`. Example asks:
- "Pull transcripts from Harvard Innovation Labs 'Startup Secrets' playlist."
- "Search r/FinancialCareers for threads on how analysts actually use DCF."
- "Get the Wharton Moneyball episodes on valuation, with signal scoring."

**2. `edgar.py`** — the empirical layer (this folder). No pip deps; stdlib only.
Set your contact UA once (SEC requires it):
```
export EDGAR_UA="Compounding-MBA techforge8yte@gmail.com"
```
Then:
```
python3 edgar.py company AAPL              # overview + filings + key financials
python3 edgar.py filings AAPL --form 10-K  # links to the real documents
python3 edgar.py facts NVDA                # XBRL fundamentals (JSON)
python3 edgar.py search "going concern"    # full-text search across all filers
```

## Distill — the note that makes it compound

Every source (a transcript, a 10-K, a thread) becomes ONE note in `~/self-mba/notes/<course>/`
using the template from `CURRICULUM.md`:

```
- Source:
- Core claim:
- Framework:
- Applies when:
- Breaks when:
- Practitioner counterpoint:
- Links: [[ ]] [[ ]]
```

Use the `deep-research` skill to distill + fact-check a batch when you want rigor;
do it by hand when you want the reps. Either way, **always close with `[[links]]`** to
prior notes — that's the compounding.

## Per-course recipe (run this each course)

1. Open `CURRICULUM.md`, find the course's source rows.
2. `research` → pull 2–4 transcripts + 1–2 Reddit threads → 1 note each.
3. `edgar.py` → pull the real company the course's *Output* targets → 1 data note.
4. **Link day:** connect new notes to prior ones.
5. **Apply:** produce the course's Output using the real data.

## Status

- [x] `edgar.py` — built, tested against live SEC data (AAPL FY2025 verified)
- [x] Data-source array — in `CURRICULUM.md`
- [ ] First real batch — Course 01 (Accounting): read a real 10-K (see `notes/01-accounting/`)
- [ ] `/schedule`d weekly auto-pull
