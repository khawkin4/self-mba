# Case 04 — Disney (DIS): license the library, or withhold it?

> **Status:** OPEN — awaiting your memo.
> **Rep type:** strategic choice cascade + coopetition + commitment.
> **Size:** **full** (~90 min) — see the menu in [MECHANISM.md](MECHANISM.md).
> No answer key. This one is genuinely contested inside the industry. Take a side.

## The brief

Disney spent the streaming era pulling its library back from rivals to feed its own service, on the
theory that exclusivity is the moat. The strategy has a cost: content that once earned high-margin
licensing revenue from a competitor now earns nothing directly, while the direct-to-consumer business
absorbs the marketing and churn expense of holding the same subscriber.

Meanwhile the industry has partially reversed: several studios resumed licensing selected titles to the
largest aggregator, arguing that the library earns more as a rented asset than as a retention tool, and
that windowing beats withholding. Disney sits on the most valuable library and the strongest brand
franchises, which makes the question sharper rather than easier — it has the most to gain from licensing
and the most to lose from training audiences to find its content elsewhere.

**Verify before you reason.** Confirm the current state of Disney's licensing posture, its DTC segment
profitability, and its content spend — from the filings, not from this brief or from memory.

**The decision:** Over the next three years, should Disney **license a defined tier of its library to
rival platforms** (and if so, which tier and on what terms), or **hold exclusivity and accept lower
near-term content monetisation** — and **what is the single thing that, if wrong, sinks your plan?**

## Pull the real data

```
python3 _ingest/edgar.py company DIS
python3 _ingest/edgar.py filings DIS --form 10-K     # segment results; Item 1A; content spend
python3 _ingest/edgar.py facts DIS                   # segment revenue/OI, capitalised content, FCF
python3 _ingest/edgar.py search "content licensing"  # how peers describe the same trade
```

Anchor the call in: DTC segment operating income and its trajectory, content spend, and the
licensing/other revenue line. Compare against at least one peer that chose the opposite policy — the
counterfactual is doing the analytical work here.

## Canon to bring to bear

`canon-lafley-martin-playing-to-win` (the cascade: where to play, how to win — and what you *won't* do) ·
`canon-brandenburger-nalebuff-coopetition` (a rival can be a complementor; the value net, not the
battlefield) · `canon-schelling-strategy-of-conflict` (a commitment only works if it is credible and
visible; exclusivity is a commitment) · `canon-helmer-7-powers` (if you can't name the *barrier*, you
don't have a moat — which of the seven is actually operating here?)

> Four frameworks. If you need a fifth, you have widened the question. Anything you reach for that is
> **not** on this list is exactly what the meta-question is hunting for.

## Your deliverable — the 1-page board memo

To the spec in `README.md`:

1. **Recommendation (BLUF)** — the call, one sentence. Not "a hybrid approach."
2. **The crux** — the pivotal, solvable challenge it turns on.
3. **Why — three reasons**, each with a real figure from the filings.
4. **The fatal risk + mitigation** — the one thing that, if wrong, sinks it.
5. **The ask** — what you want the board to approve.

**Attach a forecast.** One falsifiable statement with a probability and a resolution date.

> Two traps this case is built to catch. First, "license the non-franchise tail and keep the franchises"
> is the obvious answer — if that is your call, the memo has to defend *where* the line sits and why
> that line is defensible, or it is a tradeoffs matrix wearing a recommendation's clothes. Second, naming
> exclusivity as the moat without naming which of Helmer's seven powers it actually is scores badly on
> Evidence.

---
## YOUR MEMO
*(paste here)*

---
## RED-TEAM (after you submit)
*(six-dimension scores · the bear case · the boardroom question that sinks you · and the
meta-question: which canon note, had you read it, would have changed this memo?)*
