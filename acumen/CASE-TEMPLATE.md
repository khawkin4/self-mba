# Case NN — <COMPANY> (<TICKER>): the <topic> crux

> **Status:** OPEN — awaiting your memo.
> **Rep type:** <e.g. capital allocation + competitive strategy>.
> **Size:** full | crux-only | single-figure — see the menu in [MECHANISM.md](MECHANISM.md).
> No answer key. This is a genuinely contestable, live decision. Take a position.

## The brief

<Two or three sentences of real situation. No fabricated numbers — the figures come from the filings,
not from this brief. State the tension, not the answer.>

**The decision:** <the binary or near-binary call, stated in one sentence> — and **what is the single
thing that, if wrong, sinks your plan?**

## Pull the real data (don't take the framing above as fact — verify it)

```
python3 _ingest/edgar.py company <TICKER>
python3 _ingest/edgar.py filings <TICKER> --form 10-K   # Item 1A risk factors + MD&A
python3 _ingest/edgar.py facts <TICKER>                 # XBRL: capex, FCF, cash, debt, margins
```

Anchor every claim to a real figure. Name the comparables you are judging against.

## Canon to bring to bear

`canon-...` · `canon-...` · `canon-...`

> Three to five, no more. If you find yourself needing a sixth, the case is too broad.
> Anything you reach for that is **not** on this list is exactly what the meta-question is hunting for.

## Your deliverable

**Full** — a 1-page board memo to the spec in `README.md`: BLUF · the crux · three reasons with real
figures · the fatal risk + mitigation · the ask.

**Crux-only** — the crux in two sentences, plus the one figure that proves it, plus the bear case in
one line.

**Single-figure call** — one number pulled from the filings, what it decides, and your call. Three
sentences.

**Attach a forecast.** One falsifiable statement with a probability and a resolution date, e.g.
*"70% that gross margin is below X% by FY-end."* This is what makes calibration measurable.

**Size the call.** One line: **pass / probe / commit**, and why that size fits that probability. A
55% forecast behind "bet the company" fails, and so does a 90% forecast behind "small pilot." See
[bet-sizing-conviction](../notes/bet-sizing-conviction.md).

---
## YOUR MEMO
*(paste here)*

---
## RED-TEAM (after you submit)
*(six-dimension scores · the bear case · the boardroom question that sinks you · and the
meta-question: which canon note, had you read it, would have changed this memo?)*
