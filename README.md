# The Compounding MBA

A self-directed, master's-level business education assembled from elite free sources — Harvard, Wharton, LBS, Oxford Saïd, NYU Stern, MIT, and top practitioner content — sequenced into **24 modules** and designed to *compound* via distillation, linking, and retrieval.

**Not a playlist.** The value is the *system*: every source produces a distilled note with cross-links, failure modes, and practitioner counterpoints. Knowledge compounds through the connections between ideas, not from consuming more content.

## Quick start

**Browse the interactive site** — all 24 modules with lessons, flip cards, quizzes, and real-data examples:

```bash
open site/dist/index.html
```

Or deploy to GitHub Pages (see below).

**Read the curriculum** — the full 12-course + 12-module executive track with sources and pacing:

- [CURRICULUM.md](CURRICULUM.md)

**Start learning from zero** — the beginner on-ramp teaches financial literacy with real SEC filings:

- [learn/](learn/) — 10 four-pillar units (concept → plain language → real EDGAR example → exercise)

**Study the canon** — 82 distilled books across 23 clusters with cross-links:

- [notes/canon/CANON.md](notes/canon/CANON.md)

**Build judgment** — the Acumen Gym: real cases, real data, adversarial red-teaming:

- [acumen/](acumen/)

## What's in the repo

```
CURRICULUM.md            Full curriculum: 12 courses + 12 exec modules + sources
learn/                   Beginner on-ramp (10 units, zero to financial literacy)
  unit-01 through 10     Each: concept → understanding → real EDGAR example → exercise
  VALIDATION.md          Teaching quality flywheel
lessons/                 Interactive HTML lesson fragments (generated, per-module)
notes/
  canon/                 82 distilled books across 23 clusters
    CANON.md             Index with cross-cluster argument spines
    canon-*.md           Individual book notes (standard template)
  01-accounting/         Course-specific data notes (real 10-K analysis)
  *.md                   Practitioner notes (Tiger Sisters, EYL, Harlem Capital, etc.)
acumen/                  Judgment gym — real cases with red-team scoring
  case-01-intel.md       First case (Intel strategic inflection)
  JUDGMENT-LEDGER.md     Running scorecard across cases
site/
  build.py               Static site generator → site/dist/
  dist/                  Built interactive site (55 pages, ready to deploy)
_ingest/
  edgar.py               SEC EDGAR CLI (company/filings/facts/search — stdlib, no deps)
  pull.py                Batch transcript + Reddit puller (via research-kit)
  manifest.json          Source manifest for all 24 modules
  rescore.py             Educational Reddit re-scorer
quant-backtesting/       Quantitative backtesting research (academic + practitioner)
```

## The program structure

### Core curriculum (12 courses, ~12 months at 5 hrs/week)

| # | Course | Key sources |
|---|--------|-------------|
| 01 | Financial & Managerial Accounting | Damodaran (NYU), Accounting Stuff, HBR |
| 02 | Corporate Finance & Valuation | Damodaran full course, Wharton Moneyball |
| 03 | Microeconomics & Strategy Foundations | MRU, MIT OCW, EconTalk |
| 04 | Competitive Strategy | HBS, Porter, Acquired podcast |
| 05 | Marketing & Brand | Wharton, April Dunford, HBR JTBD |
| 06 | Operations & Supply Chain | MIT OCW, HBS ops cases |
| 07 | Data, Analytics & Decision-Making | Wharton Moneyball, StatQuest |
| 08 | Negotiation | Wharton, Chris Voss, Getting to Yes |
| 09 | Leadership & Org Behavior | LBS, Amy Edmondson, Adam Grant |
| 10 | Entrepreneurship & Venture | Harvard i-Lab, YC Startup School |
| 11 | Global Strategy & Macro | LBS, Saïd/Oxford, Odd Lots |
| 12 | Capstone — Integrative Strategy Project | Synthesis of all prior courses |

### Executive track (12 modules, the C-suite overlay)

| # | Module | Key sources |
|---|--------|-------------|
| E1 | Leading at Scale | HBR On Leadership, Stanford GSB, Masters of Scale |
| E2 | Capital Allocation | Acquired, Invest Like the Best, Damodaran |
| E3 | M&A, Deals & Restructuring | HBS deal cases, Wharton M&A |
| E4 | Corporate Governance & The Board | LBS, Saïd governance lectures |
| E5 | Transformation & Change Management | HBR, Kotter, McKinsey/BCG |
| E6 | Crisis Leadership & Resilience | HBS crisis cases, The Knowledge Project |
| E7 | Executive Presence & Comms | Stanford "Think Fast, Talk Smart" |
| E8 | Stakeholder & Investor Relations | Invest Like the Best, Odd Lots |
| E9 | Geopolitics & Macro | Odd Lots, EconTalk, LBS/Saïd |
| E10 | Digital & AI Transformation | HBR, a16z, MIT Sloan Management Review |
| E11 | Personal Operating System | The Knowledge Project, WorkLife |
| E12 | Culture as Strategy | HBR, WorkLife, Masters of Scale |

### The Canon — 82 books across 23 clusters

The reading backbone. Each distilled into a note with: core claim, framework, "applies when," "breaks when," practitioner counterpoint, and cross-links. Clusters include Strategy, Leadership, Mental Models, Negotiation, Game Theory, Platform Strategy, Systems Thinking, and more. Full index: [notes/canon/CANON.md](notes/canon/CANON.md).

### Primary data sources

| Source | What it gives you | Access |
|--------|-------------------|--------|
| **SEC EDGAR** | 10-K, 10-Q, 8-K, DEF 14A, XBRL, full-text search | `_ingest/edgar.py` |
| **Damodaran datasets** | Industry betas, margins, multiples, cost of capital | pages.stern.nyu.edu |
| **FRED** (St. Louis Fed) | Macro time series: rates, inflation, GDP | fred.stlouisfed.org |
| **World Bank / OECD / BLS** | Global development, labor, productivity | data.worldbank.org |
| **YouTube transcripts** | Lectures, founder talks, case discussions | via research skill |
| **Reddit** | Practitioner/alumni reality-check threads | via research skill |

## The learning path

```
learn/          zero → financial literacy (the on-ramp)
    ↓
lessons/        taught course material (interactive HTML)
    ↓
notes/canon/    the 82-book framework library
    ↓
acumen/         the case method: make real calls, get red-teamed
```

Each layer builds on the one below. You start at "how does a company make money" and climb to writing board memos on real strategic decisions.

## The compounding loop

Every source becomes a distilled note using this template:

```
- Source: <title / channel / url>
- Core claim: <one sentence>
- Framework: <the named model / steps>
- Applies when: <conditions>
- Breaks when: <failure modes — the part academics skip>
- Practitioner counterpoint: <does reality agree?>
- Links: [[note-x]] [[note-y]]   ← this is the compounding
```

The `[[links]]` between notes are the whole point. Porter argues with Helmer argues with Christensen on what a moat is. That disagreement, traced through real company data, is where understanding lives.

## Using the EDGAR CLI

No dependencies — stdlib Python only. Set your SEC contact header once:

```bash
export EDGAR_UA="Your-App your@email.com"
```

Then:

```bash
python3 _ingest/edgar.py company AAPL              # overview + recent filings + key financials
python3 _ingest/edgar.py filings AAPL --form 10-K  # direct links to the actual documents
python3 _ingest/edgar.py facts NVDA                # XBRL fundamentals as JSON
python3 _ingest/edgar.py search "going concern"    # full-text search across ALL filers
```

## Rebuilding the site

The interactive site is generated from the ingested corpus:

```bash
python3 site/build.py
open site/dist/index.html
```

## Deploying to GitHub Pages

The repo includes a GitHub Actions workflow that deploys the interactive site automatically on push:

```bash
git push origin master
```

The site will be available at `https://<username>.github.io/self-mba/`.

To enable: go to the repo's **Settings → Pages → Source** and select **GitHub Actions**.

## Stats

- **24 modules** (12 core + 12 executive)
- **82 distilled books** across 23 clusters
- **10 beginner units** with real EDGAR examples
- **55 interactive HTML pages** with lessons, flip cards, quizzes
- **~1.5M words** of ingested source material
- **SEC EDGAR integration** for live primary data
- **2 self-assessment exams** (recall + calibrated benchmark)

## License

Private repository — personal educational use.
