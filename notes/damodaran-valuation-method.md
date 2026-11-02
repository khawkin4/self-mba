# Damodaran's Valuation Method: Story, Numbers, Hurdle Rate, Conviction

> **Sources:** Aswath Damodaran, *Musings on Markets* (aswathdamodaran.blogspot.com, mirrored at
> aswathdamodaran.substack.com). Pulled 2026-11-01: all 28 posts from 2025-10-06 to 2026-10-28 (blog feed;
> the Substack archive skips Nov 2024–Jan 2026, so the blog is the complete copy), plus 20 methodology posts
> from the Substack archive: "Numbers and Narrative" (2014), "Narrative and Numbers" (2017), the DCF myths
> series (2015–16, Myths 1–5.5), "Putting the D in the DCF" (2015) and "The Price of Risk" (2023). All free.
> Summarized in own words; raw text stays in `_ingest/raw/2026-11-01/damodaran/`.
>
> **What it adds:** the repo's valuation material ([[unit-06-whats-a-business-worth]], the NKE rep) teaches
> *how* a DCF works. Damodaran adds the discipline around it: every input needs a story behind it, a
> market-neutral discount rate, ranges for sanity-checking inputs, and a rule linking how sure you are to
> how much you bet.
>
> **Lens:** Understand (mostly), Decide (valuation and sizing). **Serves methodology steps:** 5 (thesis,
> valuation, sizing, review) and 2 (the market-wide equity risk premium as a market-level input). Feeds
> [[portfolio-methodology-educators]].
>
> **Maps to:** Course 02 (valuation), Course 07 (decisions under uncertainty), E2 (capital allocation).
>
> ⚠ **Bias:** academic (NYU Stern) with low direct conflict, but sells books, paid certificate courses and
> runs a free data site that makes his method the default. He says openly that he is not a market-timer, then
> holds T-bills instead of adding to US equities through 2025 (Data Update 2, Jan 2026). Several valuations
> below (Anthropic, SpaceX) are his own estimates, not facts. Not advice.

---

## Core claim

Valuation is a bridge between a story and the numbers. Every number in a DCF should trace back to a part of
the story, and every part of the story should show up as a number. Numbers with no story behind them are
just modeling. A story with no numbers is just a pitch. Whatever you conclude about the stock, it is only
worth acting on if you have a reason to expect the market to correct within your holding period.

## Framework

### 1. Narrative → numbers in five steps (2014, refined in *Narrative and Numbers*, 2017)
1. **Write the story** for the business in a paragraph: what it is, how big it gets, how profitable, how
   risky. Write your own, not management's.
2. **Test it** against history (has any company actually done this?), your experience, and common sense.
   The 2025 version is the **3P test**: is it *possible*, *plausible*, *probable*? Most bad valuations
   fail at "plausible".
3. **Convert the story into value drivers:** total market size and share (→ revenue growth), target
   operating margin, reinvestment efficiency (**sales-to-capital ratio**: revenue added per $ invested), and
   risk (cost of capital, chance of failure).
4. **Connect drivers to value** with a DCF (or any model you trust).
5. **Keep the feedback loop open.** Look for the people who disagree most. When earnings reports bring news,
   classify it: does the story *change* (small tweak), *shift*, or *break*? Re-value accordingly. In his
   view a value that changes over time is normal, not a sign of error.

Worked range (Amazon, Oct 2014): the same company valued at **$32 / $175 / $468 per share** under bear / base
/ bull stories. The spread came almost entirely from the target margin (2.85% / 7.36% / 12.84%,
i.e. 25th percentile / sector average / 75th percentile) and revenue scale. The lesson: argue about the
story's margin and size, not about decimal places in the discount rate.

Applied, Oct 2026 (his Anthropic IPO valuation; his estimates):
- Story: AI becomes a $5T+ end market, and Anthropic reaches about **$1T in revenue by 2036**.
- Drivers: 27.5% target operating margin (32.5% minus a regulatory haircut), sales-to-capital of 3, cost
  of capital 9.74%. Compute commitments are counted as debt.
- Result: **equity value ≈ $1.475T.** His rule: if it is priced well above that, he sits out.
- His point about the pre-IPO market: VCs and early IPO traders are *pricing* the stock (forward multiples,
  ARR, peer groups), not valuing it. Run-rate revenue (ARR) on its own describes one part of the business
  and says little about value.

### 2. The discount rate is not where the judgment goes (DCF Myths 4.x, Data Update 5, 2026)
- **Don't put moats or management quality into the discount rate.** They belong in cash flows, margins and
  growth. Risk is about how uncertain the outcomes are, not how good they are. A wide-moat firm can be
  *riskier*, because losing the moat would destroy more value.
- **Don't add failure risk to the discount rate either.** Handle truncation risks (bankruptcy, a drug that
  fails, nationalization) with a probability: value = P(survive) × going-concern value + P(fail) ×
  distress value. Don't pad the rate to cover them.
- **Plausibility range (Jan 2026):** 80% of US firms have a USD cost of capital between **5.26% and 9.88%**
  (global: 6.28%–11.66%). A US public company valued at **14% goes on his "suspect" list**, since that is
  above the 90th percentile. Young global AI firm: start near 11.66% and glide toward ~8.65% as it matures.
  ⚠ The full tables are images in the posts and were not checked line by line.
- **Currency conversion:** add the inflation differential. For example, USD to INR adds about +1.76 pts
  (2.24% vs 4.00% IMF inflation forecasts).
- **Implication:** time spent fine-tuning the cost of capital is mostly wasted. Spend it on the story's
  revenue, margin and reinvestment.

### 3. Use the implied (forward) equity risk premium, updated monthly
- He backs the ERP out of index prices and expected cash flows (dividends + buybacks grown at earnings
  growth), instead of using historical averages. Historical ERPs range from 5.5% to 14.5% depending on the
  period chosen and are easy to bias.
- **1 Jan 2026:** S&P 500 at 6845.5, expected return **8.41%**, T-bond 4.18%, so **implied ERP 4.23%**
  (4.46% over a 3.95% riskfree rate). That is about the 1960–2025 average, below the post-2008 range, and
  well above the 2.05% low of 1999.
- Sensitivity: an ERP of 2% would make the index worth 14,834; an ERP of 6% would make it worth 4,790.
  That is how much this single input moves the answer.
- **Rule:** value companies at the *current* implied ERP (he publishes it monthly on damodaran.com). If you
  use 4% when the market is pricing 6%, every company looks cheap. You have made a market call without
  knowing it. Valuations should be **market-neutral**, and a market call should be a separate decision.
- In crises the implied ERP moves fast. It went from about 4.2% (12 Sep 2008) to nearly double within two
  months.

### 4. Terminal value is supposed to dominate (Myths 5.x)
- Most equity return historically has come from price appreciation: about 67–85% of the total return over 1-
  to 10-year horizons since 1928 (his table). So a terminal value that is 75%+ of a DCF is normal. If it is
  *small*, be suspicious.
- But **the growth-period assumptions drive the terminal value.** Higher early growth and higher ROE raise
  the base that the terminal value is built on, so they matter *more* as the terminal share rises, not
  less.
- **Cap perpetual growth at the riskfree rate** (his rule; he argues analysts who cut the riskfree rate
  to 2% but keep 5–6% nominal-GDP growth inflate value). **Negative
  terminal growth is legitimate** for declining businesses. He admits he uses it too rarely.

### 5. Margin of safety: be clear what it costs (DCF Myth 3.1)
- A margin of safety (MOS) cuts type-1 errors (buying something overvalued) and *raises* type-2 errors
  (missing bargains). It is not free. **Test:** if you hold more cash than your risk tolerance and
  liquidity needs call for, *and* you trail an index fund, your MOS is costing you money.
- A conservative value plus a MOS double- or triple-counts risk, because the DCF already adjusts for it.
- **Vary the MOS.** It should be bigger for young or uncertain businesses and for concentrated portfolios,
  and smaller for mature businesses and diversified books. One fixed 15% for a utility and a start-up makes
  no sense.

### 6. Conviction → sizing and leverage (Situational Awareness post, Aug 2026)
Conviction needs **two** beliefs: (a) your fair value is right, and (b) **the market will correct within your
time horizon.** You can be confident about the first and still lack the second.
- Sources of an edge on (a): private information (legally risky), information processing, better business
  understanding, or a pricing mistake between related assets.
- Things that make (b) more likely: a finite maturity (bonds and options converge at expiry, equities never
  have to), few market frictions, catalysts (earnings, spin-offs, activists), deep liquidity, and a long
  horizon.
- **Sizing rule:** concentrate only as far as both beliefs allow. Diversify more when holding young
  companies (pricing is noisier and catalysts are rarer). Concentrate more as your horizon gets longer.
  Investors with low conviction about young companies should spread small bets across many of them.
- **Leverage:** it magnifies your judgment, good or bad, and it **shortens your horizon**, because forced
  selling can wipe you out before the thesis is proved right. Case: Situational Awareness was up about 367%
  (Aug 2025–Jun 2026), then fell 43%+ in July 2026 (the public book about −67%) and was liquidated. A
  concentrated, levered, momentum-aligned AI bet.
- Overconfidence rises with credentials and early success. Track records under ~2 years are luck until
  proven otherwise.

### 7. Pick an investment philosophy before strategies (Mar 2026)
- Start from **where you think markets make mistakes and how they correct.** Then choose a philosophy:
  passive vs active, investing (value) vs trading (price), market timing vs stock picking. Strategies (for
  example a low-P/E screen) come out of the philosophy, not the reverse.
- You can combine philosophies only if they share a belief about market mistakes, and you name which one
  wins in a conflict.
- Check that it fits your capital, *real* time horizon (set by age, health, tuition), risk capacity and
  temperament. A mismatch means you will quit too early or fail the "sleep test".
- Account for spreads, price impact and taxes, and test for noise, before believing a strategy works.
- **Base rate (Data Update 6, 2026):** only about **28–29% of global firms earn more than their cost of
  capital**, and about 17–19% beat it by 5+ points. No region has a majority creating value. Assume most
  businesses are average.

## Applies when
- Valuing any single company for the satellite slice (step 5), especially a contested one where the bull and
  bear stories differ mainly on market size and margin.
- Checking someone else's valuation: is the cost of capital inside the 5–10% range? Is the terminal growth
  ≤ the riskfree rate? Does every number have a sentence behind it?
- Deciding position size after the valuation: use the two-belief conviction test before
  [[bet-sizing-conviction]]'s pass/probe/commit.

## Breaks when
- **Story risk dominates.** For the youngest firms, the value is almost all narrative, and a precise number
  gives false comfort. His own SpaceX ($100/share at IPO) and Anthropic figures are one person's story.
- **The CAPM/beta setup is contested.** He uses betas by industry. Investors who reject beta altogether have
  to put something else in its place. Using a margin of safety instead of a risk adjustment is the error he
  warns against.
- **Pricing beats value for long stretches.** He concedes that markets owe fundamental investors nothing.
  Momentum can swamp fundamentals, which is why the horizon belief matters.
- **Data quality.** Industry tables, margins and ERPs come from his own datasets. They are excellent, but
  built by one person and updated once a year. Several key tables in the posts are images. ⚠ Check against
  damodaran.com before using them as inputs.

## Practitioner counterpoint
- **Mauboussin** runs the same machinery in reverse: start from the price, solve for the implied
  expectations, then judge them. Damodaran's 2025 "breakeven" spreadsheet for trillion-dollar firms is that
  move (see [[portfolio-methodology-educators]], step 5).
- **Klarman / Graham** would say the margin of safety *is* the risk control. Damodaran treats it as an
  extra layer with a measurable cost ([[canon-klarman-margin-of-safety]]).
- **Feroldi** screens on quality first and treats valuation as a single line in his scorecard. Damodaran
  would say quality belongs in cash flows and only matters at a price ([[feroldi-stock-screening]]).
- The repo's [[cross-company-narrative-vs-numbers]] applies the same story-vs-numbers check to firms'
  disclosures.

## Links
[[unit-06-whats-a-business-worth]] (the DCF mechanics this builds on) · [[unit-05-growth-and-returns]] (ROIC
vs cost of capital) · [[unit-07-the-landscape-moats]] (moats go into cash flows, not the discount rate) ·
[[apply-stock-picking-nke]] (a rep to rerun with bear/base/bull stories) · [[bet-sizing-conviction]] ·
[[canon-klarman-margin-of-safety]] · [[canon-mauboussin-success-equation]] (luck vs skill in short track
records) · [[canon-kahneman-thinking-fast-and-slow]] (overconfidence) · [[canon-taleb-black-swan]]
(truncation risk) · [[cross-company-narrative-vs-numbers]] · [[feroldi-stock-screening]] ·
[[portfolio-methodology-educators]]

## The one-line habit
Before any DCF, write the story in three sentences and name the three numbers it implies (revenue in year
10, target margin, sales-to-capital). After the DCF, write whether the market must correct, and by when.
