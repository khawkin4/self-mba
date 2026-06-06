# Unit 08 — Reading the Words, Not Just the Numbers

> **For a beginner — the literacy capstone.** The numbers tell you *what happened*; the **words** of a
> 10-K tell you what management is worried about and how honestly they explain it. Learn to read both.

## Plain words first (read once)
- **10-K** — a company's detailed annual report, filed with the U.S. government, free on SEC EDGAR (Unit 01).
- **Risk Factors** (officially "Item 1A") — a section listing everything that could go wrong for the company.
- **MD&A** ("Management's Discussion & Analysis") — the section where management explains, in their own
  words, *why* the results came out as they did.
- **Boilerplate** — generic, copy-paste language that applies to almost any company and tells you little.

## ① Material — what we're learning
A 10-K isn't just tables. Two word-heavy sections carry signal a beginner can learn to read:
**Risk Factors** (what could go wrong) and **MD&A** (management's own story of the results). The numbers
are the scoreboard; the words are the *interview after the game.*

## ② Understanding — the idea in plain language
Think of it like reading a person, not just their bank statement.
- **Risk Factors** are where a company lists its dangers — but most of it is **boilerplate** ("the
  economy could weaken," "we face competition") that's true of *everyone* and means little. The skill is
  spotting the **specific, unusual** risk that's really central to *this* company. A risk that's
  concrete and particular deserves your attention; generic ones are noise.
- **MD&A** is management explaining the results. The tell is **candor vs. spin**: do they name the real
  problem plainly ("demand fell because our product got too expensive"), or hide behind vague jargon
  ("results reflected a dynamic operating environment")? Plain, specific language is a good sign;
  fog usually hides something.

You're not reading every word — you're scanning for the **specific** and the **candid**, and noticing
what they *don't* want to say plainly.

## ③ Example — the risk that was hiding in plain sight
For years before 2020, cruise lines' 10-Ks listed, among dozens of risks, something close to: *an
outbreak of contagious disease could disrupt our operations and reduce demand for cruising.* It read
like **boilerplate** — buried in a long list, easy to skip. Then **COVID-19 (2020)** made that exact
sentence devastatingly real: sailings stopped and revenue collapsed ~80% (the very numbers you read in
Unit 01).

The lesson isn't "they predicted it." It's the reading skill:
- A risk factor that is **specific and central** to how the business actually works (for a cruise line,
  "people can't or won't board ships") is worth weighing — even when it's buried as boilerplate.
- After a shock, the **MD&A** is where you check whether management names the problem honestly. A 10-K
  that says plainly "we lost $5.8B because sailings were suspended" is being candid; one that drowns the
  same fact in upbeat jargon is managing your perception.

That's the EDGAR × event bridge again, now in *words*: the filing flagged the risk; the event revealed
which words mattered.

## ④ Application — your turn
**A. Boilerplate or signal? (no computer needed.)** Two risk-factor sentences:
(1) "General economic conditions could adversely affect our results."
(2) "We depend on a single supplier for the one chip in every product we sell, and have no alternative
source." — Which is generic boilerplate, and which is a real, specific signal? *(1 is boilerplate —
true of anyone. 2 is a real, company-specific danger worth weighing.)*

**B. Candor or spin?** Management writes: "Revenue declined as the environment evolved." Rewrite it as a
candid sentence a straight-talking manager would use, *if* the real cause were that customers found a
cheaper rival. *(e.g., "Revenue fell because customers switched to a cheaper competitor.")*

**C. Optional — read a real one (only if you have this project set up).** `python3 _ingest/edgar.py
filings AAPL --form 10-K` gives links to the actual filing; open it and skim **Item 1A Risk Factors** —
notice how much is boilerplate vs. specific. No setup? Skip — A–B taught the skill.

### Check yourself
1. Which 10-K section lists what could go wrong, and which is management's own explanation of the
   results? *(Risk Factors / MD&A.)*
2. When scanning Risk Factors, what are you hunting for? *(The specific, unusual, company-central risks —
   not the generic boilerplate.)*
3. In MD&A, what's the warning sign? *(Vague jargon hiding the real cause, instead of plain, specific
   language.)*

### You've finished the beginner arcs
Literacy (01–04) → value & growth (05–06) → the landscape and the words (07–08). You can now open a real
company, read its scoreboard *and* its story, judge its health, growth, worth, and durability, and tell
boilerplate from signal.

### What's next — climb the ladder
→ **`lessons/`** (full taught courses) → **`notes/canon`** (the frameworks: Helmer, Porter, Rumelt…) →
**`acumen/`** (the case method — make real calls on real companies and get them red-teamed).
