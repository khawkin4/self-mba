# Canon → Lessons: viability plan

> The "synthesize into lessons **if viable**" judgment. Built 2026-06-05 by mapping all **23 canon
> clusters** against the **24 existing lessons** (`lessons/core-*.html` + `lessons/exec-*.html`).
> Key finding: **most canon clusters overlap a course you've already taught.** Re-teaching them as
> standalone lessons would duplicate. The high-value lesson work is the ~9 **homeless** clusters with
> no course home — and *enriching* existing lessons with the extra canon books elsewhere.

## The two moves

- **ENRICH** — the cluster maps onto an existing lesson; fold the canon books' added depth into it
  (e.g. add Cialdini + Carnegie's persuasion layer to the existing `core-08-negotiation` lesson,
  which already teaches Voss + Fisher-Ury from the same corpus).
- **NET-NEW** — no existing lesson covers it; a new `lessons/canon-<cluster>.html` is genuinely
  additive. These are the priority builds.

## The map

| # | Canon cluster | Existing home? | Verdict |
|---|---|---|---|
| 1 | Strategy (Rumelt, Porter, Lafley/Martin, Bungay) | `core-04` competitive strategy | **ENRICH 04** |
| 2 | Leadership & Presence | `core-09` leadership-ob | **ENRICH 09** |
| 3 | Mental Models & Thinking | partial (`core-07` data) | **NET-NEW** (decision-making has no real home) |
| 4 | Org Design & Mechanisms | `core-09` / `E1` | **ENRICH 09 / E1** |
| 5 | Landscape & Competitive | `core-04` | **ENRICH 04** |
| 6 | Negotiation & Influence | `core-08` (strong, same corpus) | **ENRICH 08** (add Cialdini, Carnegie) |
| 7 | Execution & Operations | `core-06` / `E5` | **ENRICH 06** |
| 8 | Culture & Change | `E12` / `E5` | **ENRICH E12 / E5** |
| 9 | **Risk, Uncertainty & Fragility** (Taleb ×2, Tetlock) | none (`E6` is crisis ops) | **NET-NEW** ⭐ |
| 10 | Product Thinking & Innovation | `core-10` entrepreneurship | **ENRICH 10** |
| 11 | **Power & Org Politics** (Pfeffer, Greene) | none | **NET-NEW** ⭐ |
| 12 | Personal Effectiveness | `E11` personal-OS | **ENRICH E11** |
| 13 | Financial Literacy for Operators | `core-02` corp finance | **ENRICH 02** |
| 14 | **Behavioral Design & Decision Science** (Nudge, Ariely, Noise, Klein, March) | none | **NET-NEW** ⭐ |
| 15 | **Game Theory & Strategic Interaction** (Dixit/Nalebuff, Schelling, Axelrod) | partial (`core-03` has one transcript) | **NET-NEW** ⭐ |
| 16 | **Network Effects & Platform Strategy** | none | **NET-NEW** ⭐ |
| 17 | **Systems Thinking & Complexity** (Senge, Sterman, Perrow, Jervis) | none | **NET-NEW** ⭐ |
| 18 | Information & Communication (Shannon, Tufte, the convos) | partial (`E7` comms) | **NET-NEW** (Shannon/Tufte/convos exceed E7) |
| 19 | Economics & Incentive Design (Mankiw, Akerlof, agency) | `core-03` micro | **ENRICH 03** |
| 20 | **History & Judgment** (Neustadt/May, Allison, Clausewitz, Thucydides) | none (`core-11` is macro) | **NET-NEW** ⭐ |
| 21 | Communication & Storytelling (Minto, Duarte, Sinek) | `E7` exec-presence | **ENRICH E7** |
| 22 | Design Thinking & Problem-Solving (Martin, Crux, Leverage Points) | partial | **ENRICH 04 / 07** |
| 23 | **Ethics & Judgment** (Badaracco, Sandel) | none | **NET-NEW** ⭐ |

## Priority net-new lessons (the additive ~9)

Ranked by additive value + how much real corpus already exists to teach from:

1. **Game Theory & Strategic Interaction** — `core-03` already has a real `yt_game-theory-in-business-strategy` transcript + econ Reddit; cleanest first build.
2. **Behavioral Design & Decision Science** — huge, practical, no home; pairs with existing `core-07`.
3. **Systems Thinking & Complexity** — the Beer Game / bullwhip teaches beautifully; ties to `core-06`.
4. **Risk, Uncertainty & Fragility** — Taleb/Tetlock; high learner demand.
5. **Network Effects & Platform Strategy** — the defining modern business model.
6. **History & Judgment** — Allison's 3 models + Thucydides Trap; distinctive.
7. **Power & Org Politics** — Pfeffer/Greene; the "uncomfortable but true" lesson.
8. **Information & Communication** — Shannon + Tufte + the conversations books.
9. **Ethics & Judgment** — Badaracco/Sandel; right-vs-right.

## The per-cluster pipeline (proven on Negotiation, 2026-06-05)

1. **Collect** — extend `_ingest/manifest.json` with a `canon` section (book-keyed YT search queries
   + Reddit subs), run `pull.py` → `_ingest/raw/<date>/canon/<cluster>/`. Reuse overlapping course
   pulls where they exist (Negotiation reused `core-08`'s Voss/Ury transcripts + r/negotiation).
2. **Analyze + synthesize** — fill each note's "practitioner counterpoint" placeholder with real
   findings + add a cited **Researched layer**. *(Done for Voss + Fisher-Ury as the worked example —
   see those two notes.)*
3. **Teach (if net-new)** — author `lessons/canon-<cluster>.html` in the Ivy & Ink style (lead,
   `viz` SVGs, `fc-grid` flashcards, `quizq`, `pitfall`, `apply-box`, `src-list`), add the cluster to
   a `canon` track in `site/build.py`, rebuild.

## Status

- [x] Pipeline proven end-to-end (Negotiation cluster, then scaled).
- [x] Cluster → lesson viability map (this file).
- [x] **Collection** — `canon` track added to `pull.py` + manifest (23 book-keyed clusters); pull ran
      → 53 YouTube transcripts + 26 Reddit pulls in `_ingest/raw/2026-06-05/canon/`.
- [x] **Enrichment** — all **82/82** notes now carry a cited *Researched layer* (workflow:
      `_ingest/canon_workflow.js`, 89 agents). **33 flagged corpus-thin** (see list below) — honest
      gaps where a book-specific transcript wasn't in the cluster pull; candidates for targeted re-pull.
- [x] **Net-new lessons (9/9)** — `lessons/canon-{game-theory, behavioral-decision, risk-fragility,
      systems-complexity, platform-strategy, history-judgment, power-politics,
      information-communication, ethics-judgment}.html`.
- [x] **Site wired** — `build.py` renders a `canon` track; rebuilt → 23 canon pages + index section.
- [ ] **Enrichment pass:** fold canon depth into the 13 ENRICH-verdict course lessons (Cialdini/Carnegie
      → `core-08`; Taleb already its own lesson; etc.).
- [ ] **Targeted re-pull** for the 33 corpus-thin notes (add book/author-specific YT queries).

### Corpus-thin notes (flagged for re-pull)
These got honest, lightly-sourced research layers because no book-specific transcript landed in the
cluster pull (the agent reused adjacent cluster material + flagged it rather than fabricate):
Ariely, Akerlof, Allison, Badaracco, Bungay, Christensen, Cialdini (Pre-Suasion), Clausewitz, Covey,
Cusumano, Goldratt, Greene, Grove (Only the Paranoid), Hagiu & Wright, Kahneman (TFS), Noise, Klein,
March, Mauboussin, Meadows (Leverage Points), Munger, Neustadt & May, Parker, Parrish, Patterson,
Perrow, Pfeffer, Rumelt (The Crux), Shannon, Shapiro & Varian, Stone, Taleb (×2), Tetlock, Thaler,
Thucydides, Tufte. Fix: add author/title-specific `yt` queries to the relevant `manifest.json`
`canon` clusters and re-run `pull.py --track canon`, then re-run the enrichment workflow on just these.
