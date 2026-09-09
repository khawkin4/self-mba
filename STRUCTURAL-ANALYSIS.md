# Structural Analysis — The Compounding MBA

> Automated scan across all layers: `learn/`, `lessons/`, `notes/canon/`, `acumen/`,
> and the built site (`site/dist/`). Last run: 2026-09-09.

---

## Health summary

| Layer | Count | Health | Notes |
|-------|-------|--------|-------|
| `learn/` beginner units | 10 | **Strong** | 69 terms defined, 4-pillar model consistent, RCL running case through Arc A |
| `notes/canon/` book notes | 82 across 23 clusters | **Strong** | 352 cross-links, zero orphans, consistent template |
| `lessons/` HTML fragments | 38 fragments across 55 pages | **Partial** | 14 of 23 canon clusters are "Sources only" (no lesson) |
| Practitioner notes | 15+ | **Strong** | 46 canon frameworks applied with real company data |
| `acumen/` judgment gym | 1 case, 0 scores | **Skeletal** | Infrastructure exists but only 1 case written |
| Built site (`site/dist/`) | 55 HTML pages | **Strong** | Interactive flip cards, quizzes, exam diagnostics |
| Cross-links (canon→canon) | 352 links | **Dense** | Most linked-to: Kahneman (29), Bezos (21), Meadows (20) |

---

## What works

### Dense cross-linking in the canon
352 canon-to-canon links with zero orphans. The most-connected nodes form natural hubs:
- **Kahneman** (*Thinking Fast and Slow*): 29 inbound — the behavioral anchor
- **Bezos** (*Shareholder Letters*): 21 inbound — the operator anchor
- **Meadows** (*Thinking in Systems*): 20 inbound — the systems anchor
- **Munger** (*Poor Charlie's Almanack*): 19 inbound — the models anchor
- **Helmer** (*7 Powers*): 17 inbound — the strategy anchor

### Practitioner bridge
46 canon frameworks are applied to real company data in practitioner notes. The Tiger Sisters
hub alone connects 30+ canon entries to actionable scripts (salary negotiation, stock picking,
wealth mechanics, private capital).

### Beginner on-ramp
10 units following the 4-pillar model (Material → Understanding → Example → Application) with
real EDGAR × event pedagogy. RCL (Royal Caribbean) serves as the running case through Arc A,
building compounding understanding.

### Argument spines
The canon isn't a reading list — it's a network of deliberate disagreements:
- Porter ↔ Helmer ↔ Christensen on moats
- Kahneman ↔ Klein on trusting intuition
- Fisher/Ury ↔ Voss on negotiation
- Rumelt ↔ Goldratt ↔ Meadows on finding the lever
- Ries ↔ Thiel on whether to iterate or go bold

---

## Gaps

### 1. Unapplied canon frameworks (33 of 82 books never applied)

These books have notes but are never used in practitioner analysis, acumen cases, or lessons.
They exist as theory without demonstrated practice.

**Strategy:** Akerlof, Brandenburger-Nalebuff, Cusumano, Lafley-Martin
**Decision-making:** Ariely, Kahneman-Noise, Klein, Parrish
**Operations:** Goldratt, Ohno, Sterman
**Systems:** Meadows (LP), Meadows (Systems), Perrow, Senge
**Leadership:** Bossidy-Charan, Bungay, Larson
**Game theory:** Axelrod, Dixit-Nalebuff, Schelling
**Ethics/history:** Badaracco, Sandel, Neustadt-May, Thucydides
**Communication:** Shannon, Tufte
**Personal:** Thaler-Sunstein
**Military/strategy:** Clausewitz
**Other:** Allison, Jervis, Martin

**Recommendation:** Pick the 10 most load-bearing (Goldratt, Meadows-Systems, Ariely,
Klein, Bungay, Lafley-Martin, Ohno, Schelling, Thaler-Sunstein, Sandel) and write one
practitioner application note for each — a case where the framework explains a real
company's outcome.

### 2. "Sources only" lesson clusters (14 of 23 clusters)

These canon clusters appear in `site/dist/` as source listings but have no authored
interactive lesson content:

- canon-behavioral-economics
- canon-communication
- canon-decision-making
- canon-economics
- canon-entrepreneurship
- canon-ethics-history
- canon-leadership
- canon-military-strategy
- canon-negotiation
- canon-operations
- canon-personal-effectiveness
- canon-platform-strategy
- canon-power-influence
- canon-systems-thinking

Only 9 clusters have actual lessons. This means the site's interactive layer covers
less than half the canon's breadth.

### 3. Undefined terms in learn/ (14 terms)

Terms used in beginner units without a "Plain words first" definition:

| Term | Unit | Risk |
|------|------|------|
| Portfolio | 10 | Novice won't understand diversification section |
| Diversified | 10 | Circular with portfolio |
| Principal (invested amount) | 10 | Confuses with "principal" (person in charge) |
| Liquidity / Liquid / Illiquid | 10 | Used in emergency fund section without definition |
| Gross income (personal) | 10 | Used for savings rate calculation |
| Private equity | 10 | Used in tier 5 without explaining |
| Venture capital | 10 | Used in tier 5 without explaining |
| Roth (IRA / 401k) | 10 | Used throughout without explaining the tax treatment |
| Tax / Tax-free | 10 | Tax advantage mentioned without explaining mechanism |
| Stock / Shares | 01 | Implicit but never formally introduced |
| Shareholder | 09 | Used without definition |
| Mortgage | 03, 10 | Used in balance sheet context |
| Perpetuity | 10 | Used in safe withdrawal rate section |
| Margin of safety | 10 | Cross-referenced but not defined in learn/ |

**Recommendation:** Add a glossary block to the top of Unit 10 defining the 12 terms
it introduces. Add stock/shares/shareholder definitions to Unit 01.

### 4. Acumen gym is skeletal

- 1 case written (Intel strategic inflection)
- 0 completed red-team scores
- JUDGMENT-LEDGER.md exists but is empty
- The infrastructure is solid (6-dimension rubric, red-team protocol) but needs cases

**Recommendation:** Write 3-5 cases that exercise the most-connected canon frameworks:
an LBO (Klarman + Jensen-Meckling), a platform cold-start (Parker + Helmer), a crisis
(Taleb + Grove), a negotiation (Fisher/Ury + Voss), and a change initiative (Kotter + Heath).

### 5. Course coverage imbalance

From the canon → course mapping:

| Coverage | Courses |
|----------|---------|
| **Heavy** (15+ notes) | 04-Competitive Strategy (17), 07-Data & Decision-Making (23), 09-Leadership & OB (22) |
| **Moderate** (8-14) | 02-Corp Finance, 03-Micro, 05-Marketing, 06-Operations, 10-Entrepreneurship |
| **Light** (< 8) | 01-Accounting, 08-Negotiation, 11-Global Strategy, 12-Capstone |
| **No canon notes** | 01-Accounting, E3-M&A |

Course 01 (Accounting) relies entirely on the EDGAR × event pedagogy in learn/ rather
than canon frameworks — this is by design but worth noting.

---

## Structural coherence map

```
                    ┌────────────────────────┐
                    │    GLOSSARY.md          │
                    │  (navigational index)   │
                    └───────────┬────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
  ┌──────────┐          ┌──────────────┐         ┌──────────┐
  │ learn/   │          │ notes/canon/ │         │ acumen/  │
  │ 10 units │ ──────── │ 82 books     │ ──────▶ │ cases    │
  │ (define) │ applies  │ 352 links    │ tests   │ (judge)  │
  └────┬─────┘          └──────┬───────┘         └──────────┘
       │                       │
       │                ┌──────┴───────┐
       │                │ practitioner │
       │                │ 15+ notes    │
       │                │ 46 applied   │
       │                └──────┬───────┘
       │                       │
       ▼                       ▼
  ┌────────────────────────────────────────┐
  │           site/dist/ (55 pages)        │
  │  Interactive lessons, quizzes, exams   │
  │  9/23 clusters have authored content   │
  └────────────────────────────────────────┘
```

**The compounding path:** A concept is *defined* in learn/, *framed* in canon notes,
*applied* in practitioner notes with real data, *tested* in acumen cases, and *taught*
interactively on the site. The glossary is the map that shows where each concept sits
in this chain and where the chain is broken.

---

*This analysis was generated by scanning all files across learn/, notes/canon/,
notes/*.md, lessons/, acumen/, and site/dist/. See [GLOSSARY.md](GLOSSARY.md) for
the full term-by-term index.*
