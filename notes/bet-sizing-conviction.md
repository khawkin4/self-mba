# Bet Sizing — Matching the Commitment to the Confidence

> Source: The Economist video "Why knowing the future doesn't always help predict markets" (YouTube `j16oj0DPv7Q`, 2026-07-28), host Rosie with capital-markets correspondent Josh Roberts, reporting an experiment run by **Elm Wealth**. Pulled 2026-10-04. Summarized in own words + brief attributed quotes, not reproductions. What it adds over the canon: the canon teaches *calibration* (Tetlock) and *survival* (Taleb, Klarman) separately. This note covers the step that connects them: turning a probability into an amount. Maps to **E2 Capital Allocation** and **Course 07**. Feeds the *sizing* line on every Acumen rep.

- **Source:** Elm Wealth "crystal ball" experiment, via The Economist (2026-07-28). Formal backbone: the Kelly criterion, as applied by practitioners in [Carver's half-Kelly](../quant-backtesting/research/robert-carver-systematic-trading.md) and [Ernest Chan's fractional Kelly](../quant-backtesting/research/ernest-chan.md).
- **Core claim:** Knowing *what* will happen is worth surprisingly little if you can't decide *how much* to commit. Calling the direction right barely separated winners from losers in the experiment. Sizing the bet to the confidence was what separated them.
- **Framework — the experiment:**
  - About 120 lay participants saw the **next day's** Wall Street Journal front page for 15 historical trading days (2008–2022). Each started with $50 and could go long or short stocks and bonds with **up to 50× leverage**.
  - Result: about half finished ahead, **about 1 in 6 went bust**, and the average ended near **$51**, roughly break-even with a crystal ball.
  - Direction hit rate was about **51%**, because prices move on news *relative to expectations* and a strong jobs number that was already priced in can still sink the market.
  - The bigger failure was sizing. Participants didn't bet more when the news made the outcome near-certain, and they used heavy leverage when they weren't sure. That combination is what produced the bankruptcies.
  - **AI models** called direction about 60% of the time but sized just as badly. Some lost money.
  - **Five professional macro traders** all made a profit and on average more than doubled their money. They were only a little better on direction. The difference: they **skipped days** with no edge and **ramped leverage hard** when conviction was high.
- **Framework — Kelly, the formal version:** for a bet paying *b*-to-1 with win probability *p*, the growth-maximizing stake is **f\* = p − (1 − p) / b** of capital.
  - Even-money bet at 51%: f\* = 2%. At 60%: 20%. At 50% or below: **zero, don't bet.**
  - Read against the experiment: a 51% edge justifies about 2% of capital, while 50× leverage stakes roughly 5,000%. The ruin was arithmetic, not bad luck.
  - Practitioners bet **half-Kelly or less**, because the *p* you plug in is itself an estimate, and overestimating it is far more costly than underestimating it (Carver cuts backtested edge by 25–33% first, then halves the bet).
- **Framework — the corporate translation (what Acumen scores):** executives rarely size a bet in percent of capital, but they always choose a commitment level:
  1. **Pass.** No edge, or the crux isn't knowable yet. A legitimate call, like the pros' no-bet days.
  2. **Probe.** A pilot, option, minority stake, or staged tranche. Sized to *buy information* when confidence is middling.
  3. **Commit.** Full capex, acquisition, or reorganization. Only when confidence is high *and* the downside doesn't threaten survival.
  - Reversibility scales the allowed size: a two-way door tolerates a larger bet at a given confidence than a one-way door ([[canon-bezos-shareholder-letters]]).
  - **Coherence test:** does the size of the recommendation follow from the stated forecast? "Bet the company" on a 55% call fails. So does "small pilot" on a 90% call where speed is the moat.
- **Applies when:** any repeated decision where you can vary the stake: capital allocation across projects, portfolio construction, hiring plans, M&A sequencing, a personal career bet.
- **Breaks when:**
  - **The probability is garbage.** Kelly multiplies your error. A miscalibrated 70% that is really 50% sizes you straight into ruin, so sizing only works on top of calibration ([[canon-tetlock-superforecasting]]).
  - **Fat tails and one-shot bets.** Kelly assumes many repeated bets with a known payoff. A single company-defining bet with an unbounded downside belongs to [[canon-taleb-black-swan]]: cap the loss first, then size.
  - **Agency.** A manager paid on upside and insulated from the downside will over-size rationally ([[canon-jensen-meckling-agency-theory]]).
  - **Small samples.** 15 days is a small experiment, and the five pros are a tiny sample. Treat the numbers as an illustration, not a law.
- **Practitioner counterpoint:** reality agrees, and is harsher. Carver's line that *"position sizing and risk management are the same thing"* is the systematic-trading version. Imran Khan's advice to find your pain threshold *"with small experiments"* before scaling is the discretionary version ([[tiger-sisters-stock-picking]]). Klarman's margin of safety is sizing expressed as price: demand a bigger discount when you're less sure ([[canon-klarman-margin-of-safety]]). The academic gap is that MBA finance teaches *which* project has positive NPV, and almost never *how much* of a finite budget to put behind an uncertain one.
- **Links:** [[canon-tetlock-superforecasting]] (the input: an honest *p*) · [[canon-duke-thinking-in-bets]] (frame it as a bet; judge the decision, not the result) · [[canon-mauboussin-success-equation]] (judge the sizing process, not one outcome) · [[canon-taleb-black-swan]] · [[canon-taleb-antifragile]] (barbell: tiny on the tails, safe on the core) · [[canon-klarman-margin-of-safety]] · [[canon-kahneman-thinking-fast-and-slow]] (overconfidence drives over-sizing) · [[canon-bezos-shareholder-letters]] (one-way vs two-way doors) · [[tiger-sisters-stock-picking]]

## The one-line habit

After every forecast, write the size: **pass / probe / commit, and why that size fits that probability.** Then let the red team check whether the two agree.
