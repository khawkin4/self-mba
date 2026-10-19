# Capital markets and M&A — how companies sell equity, and how one company pays for another

> **Part of [[wall-street-skinny-insights]]** (hub). Sibling notes: [[wss-ai-economics]] [[wss-credit-distressed]] [[wss-private-markets-wealth]] [[wss-rates-macro]] [[wss-technicals-career]] [[wss-trading-hedge-funds]]

> **Sources:** 53 Wall Street Skinny transcripts used (21 long-form videos, 32 shorts) from cluster
> `capital-markets-ma`, plus 4 more read with nothing new to add (Industry S2E6, PE Secondaries 101/201,
> *LBO in Under 3 Minutes*). Raw at `_ingest/raw/2026-10-04/media/wall-street-skinny/`. Hosts are Kristen
> Kelly (ex-Morgan Stanley IBD and equity capital markets, now teaches IB/PE technicals) and Jen Saarbach
> (ex-Morgan Stanley rates S&T). Guests: **Liz Myers** (global chair of investment banking and capital
> markets, JPMorgan; previously ran global ECM), **Scott Bok** (chairman and 16-year CEO of Greenhill,
> now part of Mizuho), Sonia Gupta (Goldman Sachs partner, co-head of biotech banking, SF) and Jesse
> Sapphire (owner of ABG Print, a self-funded acquisition). Deals covered: SpaceX IPO (June 2026), Figma
> IPO (July 2025), the planned Anthropic IPO, Ackman's pulled Pershing Square USA listing (2024), Google's
> ~$85B equity raise and $32B Wiz deal, the Netflix / Paramount / Warner Bros. Discovery contest (Dec 2025
> to Mar 2026), GameStop's bid for eBay (May 2026), 3G's take-private of Skechers (2025), Mars / Kellanova
> (2024), Amazon's Whole Foods bond deal (2017), Meta's Hyperion SPV (2025), xAI/X, Chamath's 2025 SPAC,
> Greenhill's own 2004 IPO and 2023 sale.
>
> **Maps to:** Course 02 (Corporate Finance & Valuation), **E3 (M&A, Deals & Restructuring)**, the
> core of this note, E2 (Capital Allocation), E4 (Governance: Revlon duties, dual-class control, golden
> parachutes, proxy votes, selective disclosure), E8 (Investor Relations: how the market reads a deal,
> choosing IPO investors), and Course 10/entrepreneurship for the search-fund section.
>
> ⚠ **Bias.** Both hosts are ex-sell-side. Kristen sells an M&A/IB course and plugs it in most long
> episodes, so the "traditional M&A math" (EPS accretion/dilution, relative P/E) gets presented as *the*
> lens. It is how a strategic acquirer's bankers think, not how value gets created. The IPO material
> is told from the underwriter's chair: the "perfect 20% pop" is called good engineering, when it is
> also a transfer from issuers to the banks' best trading clients (see §5 counterpoint). The JPMorgan
> guest runs the business whose fees a direct listing removes, and her case for the traditional IPO
> (§6) should be read that way. The Greenhill guest is promoting a newly published book and founded the
> boutique model he praises. The Goldman guest is recruiting. Talking about her own firm, she says it
> "sounds like a commercial, but it's not". The ETA guest owns the business he is describing. The
> Industry episodes are fiction. I use them only where the hosts explain the real mechanism and flag
> what the show gets wrong. Several transcripts are auto-captioned or machine-translated. The Anthropic
> episode in particular reads as back-translated, and it describes AI events (agents hacking
> government servers, an executive order renaming AI) that I could not verify. I use only its
> S-1/accounting content and treat its figures as soft. SpaceX and Anthropic figures post-date my own
> knowledge. They are given as the hosts stated them.

---

## What this adds to the program

- **The repo had close to nothing on capital-markets plumbing.** Before this note, a grep of `notes/`,
  `learn/`, `GLOSSARY.md` and the canon found zero hits for greenshoe, lockup, bookbuilding, IPO discount,
  collar, accretion/dilution math, breakup fee, Revlon, spin-off, mandatory convertible or index
  inclusion. [[wss-technicals-career]] now covers the interview version of the IPO pop and direct
  listing, and [[wss-ai-economics]] covers the Meta project-finance SPV. This note is the full layer
  between "what is the business worth" ([Unit 06](../learn/unit-06-whats-a-business-worth.md)) and "how
  does the money actually change hands."
- **Valuation vs. pricing vs. affordability, kept apart.** This is the most useful idea in the
  cluster. Valuation is what a thing is worth (DCF/comps). *Pricing* is the number supply and demand
  clear at on one day (an IPO, a bond book). *Affordability* is whether a particular buyer's EPS,
  leverage and currency can carry the price (M&A). Netflix walked from WBD on affordability. Paramount
  won because it didn't play by those rules.
- **How a deal gets sold, not just valued.** New in pass 2: the JPMorgan ECM chair's account of a
  modern IPO (test-the-waters meetings, cornerstone vs. anchor investors, choosing who gets shares), the
  bond-origination walk-through, block trades vs. private placements, and the direct listing. Same
  theme throughout: a narrow book misprices (Figma's pop, Meta's privately placed SPV bonds).
- **Who does the deal.** Bulge bracket vs. elite boutique, explained by the man who built one of the
  first boutiques and then sold it. Why advice-only firms exist, why they went public, and why they
  ended up back inside big banks.
- **Live 2024–26 deal arithmetic.** Every mechanism comes with the hosts' worked numbers, which I
  recompute below, flagging where theirs are off. LBO basics live in [[tiger-sisters-private-capital-101]],
  seller financing in [[tiger-sisters-wealth-mechanics]], leverage-ratio rules and private credit in
  [[wss-credit-distressed]]. This note adds the deal-side view and connects small-deal ETA to large-deal
  rollover equity.

---

## Concept map

| # | Concept | One-line definition | Why it matters | In repo? |
|---|---|---|---|---|
| 1 | Equity value vs. enterprise value | Price of the shares vs. price of the whole firm (equity + net debt) | Every headline deal number is one or the other. Confusing them produces fake "discounts" | n |
| 2 | Who does the deal: bulge bracket vs. elite boutique | Full-service banks that advise, underwrite, lend and trade vs. advice-only firms | Explains conflicts, fee incentives, who can commit financing, and career choices | partial (career angle in [[wss-technicals-career]]) |
| 3 | Debt capital markets: how a bond is born | A syndicate builds a book and prices a coupon as Treasury yield + credit spread | The most common way large companies fund deals; Amazon / Whole Foods | partial (syndication in [[wss-credit-distressed]]) |
| 4 | IPO process: valuation → pricing | Comps set a range; test-the-waters and a bookbuild of orders set the price | What lead-left banks actually do, and who gets the shares | partial |
| 5 | IPO discount and day-one pop | Deliberate ~15% underpricing so the stock trades up | Figma: ~$3B "left on the table" on day one, but back near fair value by December | partial |
| 6 | Direct listings | Listing existing shares without an underwritten offering | Removes the discount and the fee, but also the float guarantee and investor choice | partial |
| 7 | Greenshoe / stabilization | Underwriters sell 115% of the deal and either buy back or exercise an option | The mechanism that props up a new stock for 30 days | n |
| 8 | Float, lockups, index inclusion | How many shares can trade, when insiders can sell, when index funds must buy | SpaceX: 4.9% float, rewritten index rules, forced passive buying | n |
| 9 | Follow-ons and structured equity | Raising more equity after the IPO: placement, common, mandatory convert, ATM | Google's ~$85B raise; issuers sell what the market overprices | n |
| 10 | Block trades and private placements | Selling a big existing stake fast at a discount vs. negotiating with a chosen buyer | Industry's 42% "block"; who controls a company after a sell-down | n |
| 11 | SPACs, SPARCs and listed cash vehicles | A listed cash shell that buys a private company 4–5x its size | Backdoor IPO; ~30% promote; mostly poor returns; Ackman's pulled fund | partial (named only) |
| 12 | Cash vs. stock consideration and collars | How the seller is paid, and how stock price risk is split | Netflix's $27.75 quietly fell to $27.30, forcing an all-cash bid | n |
| 13 | Accretion/dilution and relative P/E | Does post-deal EPS rise or fall; which currency is "cheaper" | Why Netflix stock fell when it switched to cash | n |
| 14 | Sources and uses, financing commitments, leverage | Where every dollar of a deal comes from; how much debt the target can carry | Paramount's $110B stack; GameStop's 10x leverage hole | partial (LBO basics) |
| 15 | Contested deals: auction, hostile, deal protection | Bidding wars, tender offers, breakup/ticking fees, Revlon duties | The WBD contest moved from $19 to $31 | n |
| 16 | Spin-offs, split-offs and separations | Splitting a company into separately traded pieces | Netflix only wanted half of WBD; Kellogg → Kellanova → Mars | n |
| 17 | Rollover equity, ownership vs. control | Sellers taking stock in the combined company; voting vs. economic rights | Skechers' cash-or-unit election; PSKY holders' 0% control | partial |
| 18 | Biotech capital markets (rNPV) | Pre-revenue companies valued on probability-weighted 20–25-year DCFs | The one sector that still IPOs pre-profit; XBI trades inverse to rates | n |
| 19 | Small-deal acquisition financing (ETA) | SBA loans, seller notes, search-fund economics, permanent capital | The microcap version of LBO structuring | partial (seller financing) |

---

## 1 · Equity value vs. enterprise value

**What it is.** Equity value is what the shares are worth (share price × shares). Enterprise value
(EV) is what the *whole business* is worth to all capital providers: equity plus debt, minus cash. A
buyer who takes over a company inherits its debt, so EV is the true price of the business.

**How it works.** The hosts' house analogy: put $300k down with a $700k mortgage and you bought a $1M house,
not a $300k one.
- **xAI buying X (all stock, 2025):** headline $33B. But X carried ~$12B of debt, mostly from Musk's
  2022 LBO. EV ≈ 33 + 12 = **$45B**. In 2022 Musk paid $44B of equity on a company with ~$0.6B of
  debt, so EV ≈ $44.6B. Media said X sold "for less than he paid". In EV terms it was flat.
- **Who paid for it: xAI's outside investors.** Because the deal was all stock, xAI issued new shares
  worth $33B. An outside holder of 25% of an $80B xAI owned $20B. After the deal the equity is
  80 + 33 = $113B, so the same $20B stake is 20/113 ≈ **17.7%** (Kristen rounds to 18%; the caption's
  "20% × 80" is a slip for 25%). Their claim on xAI's future cash flows shrank by about a third in
  exchange for a share of X, priced in a round Musk himself joined.
- **Netflix / WBD:** $72B "offer value" (equity) vs. **$82.7B transaction value** (EV) for the assets
  being bought.
- **GameStop is the inverse case.** ~$11B market cap but ~$9B of cash, so its EV is *below* its equity
  value. Kristen likens it to a $100k house sitting on $500k of oil. eBay vs. GameStop is ~4x on equity
  value but ~10x on EV.

**Business significance.** Lenders, acquirers and comps all work in EV (EV/EBITDA). Shareholders
receive equity value. Every "deal size" headline should be checked for which one it is.

**Forces and impact.** LBOs push EV far above equity, because the acquired company's balance sheet
carries the debt. Cash-rich companies (GameStop, big tech) push EV below. Second-order effect: an
all-stock deal between two entities controlled by one person (xAI/X) lets that person *set* the
reference price. X's prior round at a ~$33B equity value included Musk himself, which "crystallized" the mark.

**With vs. without.** Without the EV lens you misread leverage as discount. You'd think xAI got X
cheap, or that Paramount's $108B bid was a "$72B deal".

**Applies when:** comparing companies with different capital structures; any acquisition. **Breaks
when:** debt-like items hide off balance sheet (leases, take-or-pay compute contracts; see §4) or cash is trapped.

**Channel example.** "The TRUTH about the $33bn Elon Musk's xAI paid for X"; "What the xAI / X merger
teaches us about who the real losers were in the all stock deal"; "Breaking Down the Netflix / Warner
Brothers $83bn M&A Deal."

**Counterpoint.** "Same EV in 2022 and 2025" doesn't mean fair value. It means one controlling
party marked a related-party transaction where it wanted. Kristen's own softener is that xAI's
investors were buying Musk's vision and may see an overpriced X as the cost of admission to an AI
lab. That is a rationalization of dilution, not a defense of the price. Minority holders in
controlled companies have little recourse when the controller trades with himself.

**Links:** [Unit 06](../learn/unit-06-whats-a-business-worth.md) · [[canon-klarman-margin-of-safety]] ·
[[canon-jensen-meckling-agency-theory]] (controller vs. minority holders)

---

## 2 · Who does the deal: bulge bracket vs. elite boutique

**What it is.** A *bulge bracket* bank (Goldman, Morgan Stanley, JPMorgan and peers) advises on M&A,
underwrites stock and bonds, lends, and trades. An *elite boutique* (Greenhill, Lazard, Evercore and
others) only advises: M&A, restructuring, sometimes capital-raising advice, with no balance sheet. Inside
a big bank, the investment banking division is split into *coverage* (bankers who own client
relationships) and *product groups*: M&A, equity capital markets (ECM) and debt capital markets (DCM).

**How it works** (Scott Bok, Greenhill; Liz Myers, JPMorgan):
- **The consolidation that created the boutiques.** Bok graduated from Wharton in May 1981, with fed
  funds at 20% and the Dow just under 1,000, and knew one classmate who went to Wall Street. Glass-Steagall
  still separated banking from trading. Over his first decade, British merchant banks (Warburg,
  Kleinwort Benson, Barings, Flemings) were absorbed by US, Swiss and German banks, and the tech-IPO
  specialists (Robertson Stephens, Alex. Brown, Montgomery) were bought too. By the mid-1990s about nine
  firms (six US, three European) did most investment banking.
- **The boutique pitch.** Greenhill started in 1996 as a backlash: clients sold every product by one firm
  began to doubt the firm was on their side. Bok's other motive was a mentor's line that the advisory
  business is the hot dog stand in front of the casino. The traders run the firm's results.
  Bob Greenhill had founded Morgan Stanley's M&A department with three others, when charging a fee for
  merger advice was itself new. Until then advice was a free extra to win underwriting.
- **Advice-only economics.** No balance-sheet risk, no trading, so no blow-ups, but revenue rises and
  falls with deal volume. Greenhill added **restructuring advice in 2001** as a hedge: when M&A is slow
  the economy is usually weak and companies need bankruptcy advice. Geography diversified too (Australia,
  tied to China and resources, did well while Europe's banks were struggling).
- **The boutique IPO.** After several years of ~$100M revenue, Greenhill hired Goldman on the first
  business day of 2004 and went public: ~100 people, ~16x oversubscribed, ~$500M market value after day
  one, and ~$2B within 18 months for ~125 people whose only assets were desks and phones. Lazard followed a year
  later, Evercore a year after that. Bok's 2008 anecdote: Greenhill's stock hit an all-time high the week
  Lehman failed, as the market bet the boutiques would inherit the bulge brackets' clients.
- **The round trip.** By the 2020s many firms looked like Greenhill, US public company counts had
  roughly halved since 1996, and a multi-product parent smooths the cycle (trading does well in
  volatility; M&A freezes). Greenhill sold to Mizuho.
- **The bulge-bracket pitch, from Myers.** JPMorgan offers clients the whole firm: lending, DCM, ECM,
  plus in-house experts on AI, cyber, site selection, supply chains and government relations. ECM is a
  product group raising equity (IPOs, follow-ons, private raises, converts). An ECM banker may touch ~15
  clients a week, while an M&A banker is buried in one or two deals for weeks. ECM split into sector
  teams in the early 2000s, which made it more credible with clients.

**Business significance.** The choice of adviser decides whose interests are represented. A bulge
bracket can commit billions of financing (Paramount's $54B of committed debt came from BofA, Citi and
Apollo, §14). A boutique cannot, but has fewer reasons to steer a client toward a financing it also sells.
Fees are mostly paid on completion either way.

**Forces and impact.** Regulation (Glass-Steagall's repeal in 1999; post-2008 capital rules that Bok says
the industry is still digesting) decides how much balance sheet banks can deploy. Bok counts five crises
in Greenhill's life (LTCM, dot-com, 2008, COVID, the 2022 inflation spike). His pattern: each comes from
an unexpected place, looks obvious in hindsight, is called the end of the world, isn't, and then is
forgotten. Downturns are when patient firms and people move up, because rivals step back.

**With vs. without.** Without boutiques, every adviser is also a lender and trader, and conflicts are
priced into every mandate. Without bulge brackets, no adviser could underwrite a $75B IPO or commit to a
$54B loan.

**Applies when:** advice is the product and independence is the selling point. **Breaks when:** the deal
needs a balance sheet (financing commitments, underwriting risk), or advisory revenue stalls for a few
years and fixed comp doesn't.

**Channel example.** "Elite Boutique vs. Bulge Bracket Investment Banks feat. Greenhill Chairman, Scott
Bok"; "JPMorgan Chair of Investment Banking & Capital Markets: IPOs & Equity Capital Markets 201";
"Investment Banking Hours, Mars Deal, & Google Monopoly" (on the 2024 deaths of two Bank of America
employees and the 80- and 100-hour flags banks routinely let juniors under-report).

**Counterpoint.** Boutiques are not conflict-free. A success fee pays only if the deal happens, which
biases every adviser toward doing deals. Bok himself invokes "long-term greedy" as the fix: earn trust by
sometimes saying don't buy. The Greenhill arc also cuts against the model's durability. From my own
recollection rather than the channel, Mizuho paid roughly $550M including debt in 2023, well below the
~$2B Bok cites for 2005–06. Independence was valuable while it was scarce.

**Links:** [[professional-services-leverage]] (the junior pyramid behind banking hours) ·
[[trading-floor-mechanics]] (where ECM and DCM sit) · [[wss-technicals-career]] ·
[[canon-jensen-meckling-agency-theory]] (adviser vs. client incentives)

---

## 3 · Debt capital markets: how a corporate bond is born

**What it is.** DCM is the product group that helps companies borrow by selling bonds to investors.
A group of banks (the *syndicate*) collects orders from big investors, sets the interest rate, and
promises to buy any bonds it can't sell. The new bonds then trade in the secondary market, where fixed
income sales and trading takes over. Capital markets groups straddle banking (the client) and the
trading floor (the investors).

**How it works** (the hosts' Amazon / Whole Foods walk-through):
1. **The need.** Amazon buys Whole Foods for $13.7B and chooses to borrow rather than use cash or stock.
   M&A bankers (Goldman, in the hosts' telling) advise on the deal. A syndicate (Goldman with BofA and
   JPMorgan) arranges the bonds.
2. **Underwriting.** The syndicate commits to take down the whole issue if investors won't. Its fee is
   the gap between the price it pays the issuer and the price it sells at: Kristen's illustration is
   buying at 98 and selling at 100.
3. **The coupon build.** Rate = risk-free Treasury yield for that maturity + the issuer's credit spread.
   Illustration: 10-year Treasury at 5% + Amazon's spread of 1% = **6%**. Longer bonds pay more (their
   example: 40-year at ~8% vs. 10-year at ~6%), and riskier issuers pay wider spreads.
4. **Building the book.** DCM bankers work with credit salespeople, who canvass Fidelity, BlackRock,
   Vanguard and others. A hot deal is "oversubscribed" (the hosts' example: $45B of orders for $13.7B of
   bonds). Excess demand tightens the price talk, so the issuer pays a lower spread.
5. **Pricing day.** Issuer treasury team, syndicate and traders are on one call. At the chosen moment the
   lead's trader calls a price on the on-the-run Treasury, the spread is added, and the coupon is fixed.
   Timing matters: Kristen's mortgage-lock story is the household version of an issuer pricing just
   before a 75bp rally.
6. **Who does what.** Investment-grade (IG) DCM serves strong credits. **Leveraged finance** serves
   high-yield ("junk") issuers, including LBOs, which is why it feeds private equity. Converts, project
   finance and structured products are separate product teams.

**The private-placement contrast** (Meta, Oct 2025; detail in [[wss-ai-economics]] §7). Meta's ~$30B
Hyperion data center was funded through an SPV owned ~80% by Blue Owl, with ~$27B of bonds sold as a
**144A private placement**. They were rated A+ (Meta itself is AA−) and priced at ~6.58%, about **100bp
wide of Meta's own curve** (initial talk was 150bp). PIMCO took ~$18B and was soon up ~10 points, about
**$1.8B** on paper, though part of that was a Treasury rally. Days later Meta sold **$30B of public bonds
in six tranches** at roughly +90bp (30-year) and +105bp (40-year), around 100bp tighter. Jen's verdict: a
narrow private book mispriced the deal. The same lesson as Figma's pop (§5), in bonds.

**Business significance.** Bonds let a company fix its cost of money for 10–40 years without giving
up ownership. The syndicate earns the spread and takes the risk of a failed deal. Investors earn the
coupon. The credit rating sets the issuer's cost, which is why big tech guards its ratings.

**Forces and impact.** The Treasury curve moves every issuer's cost at once. Ratings and spreads move
with the issuer's leverage. Myers adds a sequencing rule: when a company needs both, do the IPO first,
because public reporting and a visible equity value make the debt easier to sell. Rating agencies
matter even for sovereigns: Moody's was the last of the three to downgrade the US (May 2025; S&P in 2011,
Fitch in 2023), and markets barely reacted.

**With vs. without.** Without a bond market, Amazon depends on one bank's balance sheet for $13.7B over
40 years, and no bank wants that. Without syndicate underwriting, the issuer carries the risk of a half-
filled book on the day it needs the money.

**Applies when:** large, rated issuers with predictable cash flows. **Breaks when:** markets shut
(the syndicate is left holding a "hung" deal), or a private book substitutes for price discovery (Meta).

**Channel example.** "5. Debt Capital Markets 101: Where Do Bonds Come From?"; "Meta & xAI as Project
Finance 101."

**Counterpoint.** The hosts flag their own simplifications. Two more: a 2-point underwriting spread is
high-yield territory. IG gross spreads are much smaller, usually well under 1% (my figure, not the
channel's). And Amazon actually sold about $16B of bonds in August 2017, more than the purchase price
(again my recollection). The 98/100 and 5% + 1% figures are teaching numbers. Treat them as such.

**Links:** [[wss-credit-distressed]] (syndicated loans, private credit, leverage rules) ·
[[wss-rates-macro]] (what moves the Treasury leg) · [[trading-floor-mechanics]]

---

## 4 · The IPO process: valuation → pricing, test-the-waters, bookbuild, syndicate

**What it is.** An IPO sells a small slice of a private company to public investors for the first
time. Bankers first estimate *value* (comps, sometimes DCF). Then they *price* the deal by collecting
investor orders and choosing the price at which demand clears. Most of the work happens before the
orders: months of educating investors.

**Why companies go public** (Myers): growth capital, which is dearer when private; a currency for
employee compensation; and a currency for acquisitions, since a listed buyer has stock to offer and
easier access to debt. Sponsor-backed IPOs are often **all primary, used to delever**: public investors
won't carry LBO-level debt. When a company is cash-generative, the IPO can be all secondary, but holders
are often reluctant to sell at the IPO discount, so bankers "pull the secondary out" of them. A sponsor
that IPOs rather than sells outright is signaling belief: it gives up a ~25% control premium for a
~15% discount, betting on selling later at higher prices.

**How it works.**
1. **Test-the-waters.** Since the JOBS Act (2012), first for emerging growth companies and then for
   everyone, companies can meet public investors months or years before filing. Myers describes two or
   three rounds: a company overview, then the growth algorithm and margins, then Q&A. Historicals arrive
   only with the red herring. Before this, investors got one 45–50-minute meeting about two weeks before
   pricing.
2. **Research analysts** at each underwriter build models and educate investors, so management doesn't
   have to coach every fund and isn't committed to every forecast.
3. **Value with comps** (the hosts' illustrative Anthropic walk-through). 12–13x EV/revenue on expected
   2028 revenue of $200B → **$2.4–2.6T EV**. Add net cash (the host assumes $50B; captioned as "million")
   → ~$2.45–2.65T equity. Apply a ~15% IPO discount → ~$2.08–2.25T. Divide by an assumed 10B shares → a
   **$208–225 range**. The range appears in the amended S-1 (the "red herring") when the roadshow starts.
4. **Cornerstones and anchors.** A **cornerstone** (BlackRock, Fidelity, Capital, T. Rowe in Myers's
   examples) commits on the cover to ~10–20% of the deal and may see the S-1 early under NDA. An
   **anchor** is an expected opening order of ~5–10% that bankers line up in a "shadow book" to set the
   range and size. Anchors get allocation priority. Too much in cornerstones shrinks the float other
   investors can buy.
5. **Bookbuild.** About seven days (five if markets are rocky). Investors place **limit orders** (up to a
   price) or **market orders** (fine anywhere in the range). Total demand ÷ shares offered = times
   oversubscribed (10B ÷ 500M = 20x). A hot book raises the range, upsizes the deal, or adds secondary.
6. **Price and allocate** the night before trading. Myers frames allocation as management choosing its
   partners: who did the work, who will hold. File the 424B4 with the final price, shares and proceeds.
7. **Primary vs. secondary.** Primary shares are new and the cash goes to the company. Secondary shares
   are existing holders cashing out. SpaceX was 100% primary. Figma was 12.5M primary / 24.5M secondary.
   Primary proceeds raise post-money equity value: $95 pre-money + $5 raised = $100 post. Damodaran moved
   his SpaceX value from $1.2T to ~$1.3T for that reason.

**Who buys.** Three buckets (Myers): long-only mutual funds, hedge funds, and sovereign wealth funds,
plus retail. Retail was 10–20% of most IPOs in the late 1990s, was squeezed out, and is coming back.
Banks treat it as price-insensitive and following the institutions. Myers disputes the "hedge funds flip"
stereotype: hedged funds can hold longer, and long-only funds can sell on day one. Banks track every
account's past behavior to predict who will hold.

**Timing: the "IPO dashboard."** Dials for the macro backdrop (Fed, inflation, tariffs), recent IPO
receptivity (priced above, within or below range) and aftermarket performance. Don't launch before an
uncertain Fed meeting: once launched you are exposed for seven days, and postponing hurts. Myers expected
2025 US IPO volume up ~35%, with Q2 usually the busiest quarter because Q1 waits on year-end numbers.

**Syndicate and fees.** **Lead left** is listed first, runs the book, has final say on pricing, does the
most work and takes the most fees. Then other bookrunners, then co-managers. "Rack rate" gross spread is
6–7% for small IPOs. Mega-deals pay far less: Facebook ~1.1% (Morgan Stanley as lead left earned ~$68M
vs. ~$35M and ~$25M for JPM and Goldman, per Kristen); SpaceX reportedly **75bp** on ~$75B; Google's
follow-on ~1%. Bank order in press releases is read as a tell (Morgan Stanley listed first on SpaceX).

**Business significance.** The company buys certification, distribution and price discovery. The bank
earns fees and league-table rank. Rank matters more than any one fee: Kristen says the fumbled 2012
Facebook IPO cost MS "years" of lead-left mandates.

**Forces and impact.** IPO windows open and close with rates and risk appetite (2025's April "tariff
tantrum" and the SEC shutdown both stalled deals). Companies stay private longer when private capital is
abundant. A queue of mega-IPOs (SpaceX, Anthropic, OpenAI) pulls money *out* of existing holdings (§8).
Banks now use internal LLMs to draft the first S-1 and committee memos (JPMorgan, per Myers).

**With vs. without.** Without a bookbuild, price is set by fiat. **SpaceX did exactly that**: per a
hedge fund source quoted by Matt Levine, Musk set a take-it-or-leave-it $135, reportedly the price that
made him a trillionaire, against $250B of demand for $75B of stock (~3.3x; hosts say "four times"). The
alternatives are a direct listing (§6) or a SPAC (§11).

**Applies when:** issuer has a story institutions can comp. **Breaks when:** no comparable exists
(SpaceX; hosts admit DCFs get "reverse-engineered" to the number the client wants) or the S-1 reveals
things the narrative hid.

**Reading the S-1 (Anthropic leak, via Reuters, as relayed):** SaaS-style *run-rate* revenue (last
month × 12) vs. historical revenue (~$4.6B in 2025); a $42B 2025 loss of which ~$34B was a
non-cash charge on converting financing instruments, which private companies run through the P&L;
~25% of revenue from two customers not on long-term contracts; and large compute commitments that sit
in footnotes rather than as debt or leases, even though the neoclouds on the other side borrow against
those same contracts. That last point is the EV caveat from §1 in practice.

**Channel example.** "JPMorgan Chair of Investment Banking & Capital Markets: IPOs & Equity Capital
Markets 201"; "The truth about whether Anthropic could IPO for a $3 trillion valuation" (captions say
"billion" throughout; the hosts mean trillion); "Did Goldman Sachs just lose SpaceX IPO to Morgan Stanley?"

**Counterpoint.** Comps "anchor" an IPO only if the peer multiple is itself sane. When the comp set is
other richly valued AI names, it's circular. On SpaceX, with no fundamental anchor, perpetual-futures
markets at ~$174 (= $135 + ~29%) became the coordination point. And "management chooses its partners" is
the flattering name for the allocation power that critics say banks use to reward commission-paying
clients. Test-the-waters also lets the best-connected funds form views months before everyone else.

**Links:** [[sec-filing-intelligence]] · [[canon-akerlof-market-for-lemons]] (why issuers must
discount: they know more than buyers) · [[trading-floor-mechanics]]

---

## 5 · The IPO discount and the day-one pop

**What it is.** Underwriters deliberately price ~15% below where they expect the stock to trade
"fully distributed", so first-day buyers see a gain and the deal has momentum. A pop much bigger than
that looks like the seller sold too cheap, but the day-one price isn't the only test.

**How it works: the Figma arithmetic** (July 2025, hosts' figures):
- Range talk $30–32, priced **$33**, ~40x oversubscribed (reported).
- Offering: 12.5M primary + 24.5M secondary = **37M shares** → 37M × $33 ≈ **$1.22B raised**.
- 585M fully diluted shares × $33 = **$19.3B** valuation. That roughly equals Adobe's failed $20B
  bid, but a takeover includes a control premium and an IPO includes a discount.
- Day-one close ~**$115** (+~250%). Gap ≈ $82/share × 37M ≈ **$3.0B left on the table** on day one,
  split between Figma and its VCs (Index, Greylock).
- **Five months later** (Dec 2025, in the JPMorgan episode) the stock was ~**$39**. Grossing $33 up for a
  15% discount gives 33 / 0.85 ≈ **$38.8**. By that test the IPO was priced about right, and the pop was
  a burst of excitement among day-one traders.

**SpaceX** (June 2026) is the opposite: priced $135, opened/closed day one at **$160.95 (+19.2%)**, which
Kristen calls the "perfect 20% pop," later traded to ~$200 and back to ~$154.

**Business significance.** Underpricing is a cost borne by issuers and selling holders. The gain goes to
whoever got allocations, mostly large institutions that are also the bank's commission-paying clients.
Myers adds that some tech issuers have *wanted* a big run as a sign of scarcity and success. The direct
listing (§6) was invented by issuers who didn't.

**Forces and impact.** Banks are rewarded for a deal that trades well (reputation, future mandates)
and punished hard for a broken deal (Facebook). That pushes them toward conservative pricing.
Second-order effect: a blowout pop resets the next issuer's expectations (Jen: after your neighbor sells
at 1.5, you list at 1.1, not 1.5), which can reopen an IPO window.

**With vs. without.** No discount: shaky first-day trading, buyers who feel "stuffed," weaker follow-on
demand. Too much discount: a multi-billion transfer, plus existing holders sitting on paper gains
they can't touch until lockup expiry.

**Applies when:** information asymmetry and allocation-driven demand. **Breaks when:** retail
allocations and over-pricing collide (Facebook priced at $38, broke issue), or pricing is
dictated (SpaceX).

**Channel example.** "Why Figma's stock price tripling the day of its IPO a bad thing"; "How Goldman Sachs
and Elon Musk pulled off the perfect IPO"; the Figma exchange in "JPMorgan Chair… ECM 201."

**Counterpoint.** Both readings of Figma hold at once. Measured by fair value, the discount was ~15% as
designed. Measured by what sellers could have got, the 24.5M secondary shares were sold at $33 into a
market that paid $115 that afternoon, and allocated buyers who sold on day one captured it. Academic
work (Ritter et al.) finds average US first-day returns in the high teens, with documented allocation
conflicts. On SpaceX, the "perfect pop" may simply be the futures market's self-fulfilling forecast (§4),
not skill.

**Links:** [[canon-kahneman-thinking-fast-and-slow]] (anchoring on the prior deal) ·
[[entrepreneurship-operator-playbook]] (dilution from the founder's side)

---

## 6 · Direct listings: going public without an offering

**What it is.** A direct listing puts a company's existing shares on an exchange without an
underwritten offering. No new shares are sold to a book of investors. The opening price comes from
whatever supply and demand meet on the first day. It suits companies that want liquidity for early
holders and employees but don't need to raise money.

**How it works** (Myers's comparison with a traditional IPO):
- **What disappears:** the bookbuild, test-the-waters meetings, deep bank due diligence, a coordinated
  research launch (in an IPO, underwriters' analysts publish at a set date as an aftermarket catalyst),
  the greenshoe, and the issuer's choice of investors.
- **What becomes unknown:** float. In an IPO the prospectus says exactly how many shares are for sale,
  primary and secondary, and who is selling. In a direct listing float is whatever existing holders
  decide to sell, which nobody commits to in advance.
- **What is saved:** the gross spread and the deliberate ~15% discount. Figma's ~$3B day-one gap
  (§5) is the argument critics made for why it should have listed directly.
- **Track record as relayed:** Spotify (2018) and Slack (2019) pioneered it. Slack was later bought by
  Salesforce and Spotify trades well. Others traded worse, which Myers notes is true of IPOs too.

**Business significance.** A direct listing shifts power from underwriters to the issuer and its
existing holders, and shifts price discovery from a negotiated book to the open market. Banks lose most
of the fee. Issuers lose the ability to raise primary capital in the traditional form and to pick holders.

**Forces and impact.** Demand for direct listings rises after blowout pops and fades when markets are
choppy and a guaranteed raise matters. From my knowledge rather than the channel: NYSE and Nasdaq rule
changes in 2020 let companies raise primary capital in a direct listing, yet few have used it.

**With vs. without.** With only IPOs, every issuer pays the discount and the spread. With direct
listings, a well-known brand with dispersed holders can skip both, at the cost of an uncertain float and
a first day nobody stabilizes.

**Applies when:** strong brand, no capital need, many willing secondary sellers, investors who can value
it unaided. **Breaks when:** the company needs money, the story needs explaining, or few holders want to
sell (thin float, volatile price).

**Channel example.** "JPMorgan Chair of Investment Banking & Capital Markets: IPOs & Equity Capital
Markets 201" (Kristen's Figma question).

**Counterpoint.** Every disadvantage Myers lists is a service JPMorgan sells. Some are real: float
certainty and research coverage matter to long-only funds. "Choosing your partners" is weaker. Holders of
a liquid stock change daily whatever the issuer chose at pricing. The best evidence for her side is the
market's own choice: few large companies have direct-listed since 2021.

**Links:** [[wss-technicals-career]] (interview version: IPO vs. direct listing) ·
[[market-structure-24-5-trading]] (opening auctions)

---

## 7 · The greenshoe (over-allotment) and stabilization

**What it is.** Underwriters sell up to 15% *more* shares than the deal size, creating a short
position. The issuer gives them an option, the "greenshoe", to buy that extra 15% at the IPO price. The
short plus the option lets banks support the stock if it falls, at no loss if it rises.

**How it works.** SpaceX: deal size $75B, but banks sold ~$85B. 15% × $75B = $11.25B, so ~$86B. The
arithmetic checks against the float: 639M shares floated × $135 ≈ $86B.
- **Stock falls below $135** in the first 30 days: banks buy shares in the market to cover the short.
  That buying is the price support. They sold at $135 and bought lower, so they *profit*. This is why
  Kristen titles a short "Goldman and Morgan Stanley were short SpaceX."
- **Stock rises:** banks exercise the greenshoe, buy the extra shares from SpaceX at $135, and deliver them.
  No market purchase is needed, nobody loses, and the issuer raised 15% more.

**Business significance.** It is a built-in buyer of last resort for the first month. The issuer gets
upside from extra proceeds. Underwriters get a hedge that turns stabilization from a cost into a
possible gain.

**Forces and impact.** Underwriting banks reportedly don't lend stock to short sellers for ~30 days
post-IPO. The hosts couldn't find the written SEC rule but say it is common practice. With every major
bank in the syndicate (only Jefferies absent on SpaceX), all insiders locked up, and no borrow available,
there were "only buyers". Supply restriction plus the shoe made the pop close to mechanical. A direct
listing (§6) has none of this support.

**With vs. without.** Without the shoe, a weak debut has no natural bid and can spiral below issue. That
is the "broken deal" that costs banks future mandates. The money underwriters make in a falling scenario
is small next to the franchise damage. The hosts are right that banks don't *want* the profitable outcome.

**Applies when:** the first ~30 days of trading. **Breaks when:** selling overwhelms the 15% cushion.
Stabilization is finite: Facebook fell through issue despite support.

**Channel example.** "Why Goldman Sachs and Morgan Stanley were short SpaceX"; "SpaceX IPO: 99% of investors had no idea."

**Counterpoint.** "Banks are short" is technically true but misleading in spirit. The short is fully
hedged by the option on the upside. The real economic exposure is reputational, not directional.

**Links:** [[trading-floor-mechanics]] · [[market-structure-24-5-trading]]

---

## 8 · Float, lockups and index inclusion: who has to buy and who is allowed to sell

**What it is.** *Float* is the share of a company that can actually trade. A *lockup* bars insiders
from selling for a set period, typically 180 days. *Index inclusion* forces passive funds tracking that
index to buy the stock. For a mega-IPO with a tiny float, these three rules set the supply/demand
balance for the first year.

**How it works** (SpaceX, hosts' figures):
- **639M of 13.1B shares float = 4.9%** (typical IPO float is 10–20%). Market cap ~$2T, but ~95% is locked.
- Lockups: Musk ~366 days. Other insiders get shorter, *conditional* windows: share price must trade ~30%
  above IPO for a set number of days, plus a wait until after Q2 earnings, with staggered unlocks (Aug 6
  and Aug 21; ~1B shares 2 days after Q2 earnings). Hurdled lockups are SPAC-like (§11).
- **Index rules, rewritten for this deal:**
  - **S&P 500** kept its rules (12-month seasoning, four quarters of positive GAAP net income, float
    minimums) and voted down every mega-cap exemption. It changed only the investable-weight-factor
    test: a stock now qualifies if its float-adjusted cap ≥10% of the total cap of the 100th-largest
    company in the S&P TMI. SpaceX isn't GAAP-profitable, so it's out for now.
  - **Nasdaq-100** cut seasoning from 3 months to **15 days**, waived the 10% float minimum, and, for
    low-float new listings, weights at **3x float** rather than full cap: 4.9% → 14.7%.
  - **Russell** added SpaceX June 29, est. $3–4B of passive buying. The Nasdaq addition (July 7) was est. ≥$8B.
- The supposed design trick: indices weight by float, so **every unlock raises the float and forces
  index funds to buy** just as insiders sell. Leveraged 2x single-stock ETFs add further mechanical demand.
- After lockups, large holders typically sell down through block trades or marketed follow-ons (§10).

**Business significance.** For issuers, index inclusion is a multi-billion guaranteed bid. For
passive investors, a polarizing mega-cap enters "the market" by committee decision, not by choice.
For active funds, the IPO is funded by selling something else.

**Forces and impact.** Jen's second-order effect: money isn't infinite, so investors fund SpaceX by selling
the closest substitute (Tesla, "the Elon trade"). That pushes **single-name implied vol to a record
spread over index vol** (VIX ~16; Tesla 30-day IV ~45% vs. S&P ~12%). This makes the *dispersion trade*
(short index vol, long single-name vol, i.e. short correlation) newly attractive. Paul Tudor Jones and
Michael Burry are cited comparing the IPO supply wave to the run-up to the 2000–01 dot-com crash. The CBOE
equity put/call ratio at ~0.44 vs. a 0.6–0.7 norm signals crowded bullishness.

**With vs. without.** Without float-adjusted inclusion, a 4.9%-float stock would get a full $2T
weight and force buyers to chase a liquidity-starved stock. Without inclusion at all, Kristen argues,
index holders get hit anyway as money rotates out of incumbents into the excluded name. That is why she
grudgingly supports the Nasdaq change.

**Applies when:** low-float mega-listings. **Breaks when:** unlock supply outruns forced index demand.
The hosts' Aug-unlock analysis expects the Nasdaq reweight only "around April," so there is a timing gap.

**Channel example.** "SpaceX Just Rewrote the Rules of the Stock Market"; "The truth about SpaceX Q2
earnings"; "SpaceX IPO: what Goldman Sachs bankers know about what comes next."

**Counterpoint.** Calling this "beautifully engineered" assumes the unlock-to-index-buy match is
large. Their own numbers (Russell $3–4B, Nasdaq ~$8B) are small next to ~95% of a $2T company unlocking
within 12 months. The structural risk is that *passive* investors end up as exit liquidity for VCs whose
fund lives force them to sell, which the hosts mention in passing. (The LP-side of that exit is
[[wss-private-markets-wealth]]'s secondaries material.)

**Links:** [[market-structure-24-5-institutional-response]] · [[market-structure-24-5-trading]] ·
[[canon-taleb-black-swan]]

---

## 9 · Follow-ons and structured equity: Google's ~$85B raise

**What it is.** A follow-on (seasoned) offering is equity sold by an already-public company, usually six
months or more after the IPO. It can be plain common stock, or wrapped in structures that change how
much dilution the issuer accepts at each future share price. Myers lists ECM's toolkit: IPOs, follow-ons,
private raises for companies not ready to list, and convertibles.

**How it works.** Google's headline ~$85B (larger than the SpaceX IPO) had four parts:
1. **Private placement to Berkshire Hathaway** of A and C shares, at a discount. That buys a large, steady,
   non-flipping holder (the negotiated route of §10).
2. **~$19B common stock** (A and C classes; Goldman lead left).
3. **Mandatory convertible preferred**, ~6–6.25% dividend, converts to common in 3 years
   *no matter what*. Per $1,000 at a $100 reference price with a 25% cap:
   - share price ≤ $100 → 10 shares (holder bears full downside)
   - $100–125 → shares = 1,000/price, so the holder gets ~$1,000 back (debt-like)
   - ≥ $125 → 8 shares (holder keeps upside on 8 shares, e.g. 8 × $200 = $1,600)
   - Google then **bought a capped call** (long 125 call, short 150 call) from the banks, so its
     *net* issuance falls to 1,000/150 ≈ **6.67 shares** above $150. The issuer has bought back its upside.
4. **~$40B at-the-market (ATM) program:** agents dribble shares into the market at Google's discretion,
   with the stated use of paying employees' taxes on stock comp instead of net-share-settling it.

**Business significance.** Even a "cash printing machine" raises equity when the AI capex race needs
it. Converts let issuers *sell volatility*: investors pay for optionality, and the issuer gets cheaper
financing (a convert coupon of ~2% where straight debt would cost ~10%, Kristen's stylized example;
Myers: debt with an equity option attached "to buy down the interest rate"). Who buys matters: convertible
arbitrage funds buy the convert and short the stock, so pricing has to anticipate that selling.

**Forces and impact.** Jen's market reading: issuers sell what's rich. Equity valuations are high,
single-name vol is high, and call skew is rich (put/call ~0.44), so the issuer sells all three. Same logic
as AI debt issuance signaling tight credit spreads. Fee note: follow-ons usually pay less than IPOs, but
Google's ~1% beat SpaceX's 75bp. Tax tailwind: 100% first-year capex expensing under the current law
rewards spending *now*. In 2008, converts were the only equity many banks could raise (Kristen's
converts desk sat beside TARP rescue work).

**With vs. without.** With only common stock, Google issues full dilution at today's price. Without
the ATM, every raise is a discrete, signal-heavy block. With the mandatory + capped call, dilution
is capped if the stock rallies.

**Applies when:** issuer is bullish on its own stock and vol is expensive. **Breaks when:** stock
falls. Mandatory holders then convert into 10 shares worth less, and the issuer gave away a 6% dividend for
equity it could have sold outright.

**Channel example.** "The Truth About Google's Record-Breaking $85 Billion Equity Raise"; "Google's $17
billion Equity Deal to Fund AI Explained."

**Counterpoint.** Kristen herself flags the puzzle. Mandatories with a *debt* host are standard because
interest is tax-deductible. Preferred is usually for unprofitable issuers. And capped calls replaced the
classic tax-advantaged bond-hedge-plus-warrant structure. She didn't resolve it, and I can't either. (Also:
"$85B" mixes committed common with a $40B ATM that may never be fully drawn.)

**Links:** [[canon-taleb-antifragile]] (who is long vs. short optionality) · [[trading-floor-mechanics]]

---

## 10 · Block trades and private placements: selling a big stake

**What it is.** A **block trade** sells a large existing stake in a listed company in one go, usually
overnight, through a bank to institutional buyers at a discount to the last price. A **private
placement** sells new or existing shares to a buyer the seller chooses, at a negotiated price, outside the
open market. Blocks are about speed and anonymity. Placements are about who ends up owning the shares.

**How it works** (Kristen and Jen on Industry S2E2–S2E3, plus real cases):
- **Size.** Kristen (backed by her ex-ECM husband): most blocks are roughly 1–10% of a company. A stake
  much larger than that is placed privately, so the seller knows and vets the buyer. The show's 42% block
  is the plot hole she keeps returning to.
- **The arithmetic of the show's block.** ~75M shares at ~$45 ≈ **$3.4B**. If that is 42%, the company
  is 3.4 / 0.42 ≈ **$8B**, matching the CEO's own "$8 billion" valuation, and ~179M shares outstanding.
- **Bank risk.** In S2E2 the bank owned the block and it was close to "hung" (unsold). The fund that
  stepped in bought at a discount once the desk was in maximum pain. Buyers who know a bank is stuck
  can extract price, which is why desks watch who knows they hold a position.
- **Pre-arranged cross.** When a buyer and seller agree privately (half of an 18% holder's stake, ~9%, to
  the 42% holder), the bank executes both sides: seller at $48.00, buyer at $48.25. The desk keeps the
  $0.25. On ~9% of ~179M shares ≈ 16M shares, that is ≈ **$4M**. It is done before the open to lock the
  price and stop others trading ahead of it.
- **Control after the trade.** 42% + 9% = 51%, a majority. Moments earlier the board had asked the new
  holder to sign a proxy form handing over his votes, which the hosts call a red flag on both sides.
- **Selective disclosure.** In the plot the company hides an analysis (a price cut would require a
  dividend cut) from most investors and shares it with a favored buyer. Kristen's point: in the US every
  investor must get material information at the same time (8-Ks, Reg FD), so this is illegal.
- **Real placements in the cluster:** Google's discounted Berkshire placement (§9); the post-SPAC
  private placement that funds the merger (§11).
- **"Block" in futures means the same thing:** a large trade negotiated off the order book. Jen's example:
  someone sold **78,000** June 10-year Treasury futures in early London hours, the biggest such block in
  at least 12 years. Risk was **$5.1M per basis point** (≈ $65 per bp per contract), so a 5–10bp selloff
  meant a gain of roughly $25–50M if it wasn't a hedge.

**Business significance.** Sellers (PE after a lockup, founders, VCs, a parent selling down a
subsidiary) get size and certainty fast. Buyers get stock at a discount. The bank earns a spread or fee
and, in a bought block, carries the price risk overnight. Placements let the issuer or seller pick a
holder it trusts, which matters when the stake carries control.

**Forces and impact.** Lockup expiries and fund-life deadlines create supply. Myers's sponsors exit an
IPO'd company in stages, ideally each at a higher price. Each stage is a block or marketed follow-on. A
large overhang of locked-up stock (SpaceX, §8) caps rallies because buyers expect the blocks.

**With vs. without.** Without blocks, a holder dribbles shares out over weeks, signaling its exit and
pressing the price the whole time. The ATM (§9) is the issuer's version. Without placements, control
stakes go to whoever shows up in the market.

**Applies when:** liquid stocks, stakes small relative to trading volume. **Breaks when:** the stake is
large enough to change control (then negotiate), or the bank misjudges demand and is left holding it.

**Channel example.** Industry S2E3 "The Fool" (block trades, proxy votes, private placement); "Largest 10
Year Treasury Futures Block Trade EVER?"

**Counterpoint.** The show is fiction and the hosts' S2E2 episode, which explains blocks vs. other equity
offerings directly, is missing (Gaps). Block discounts for liquid large caps are often low single digits
(my figure, not the channel's). And Kristen's "just do a private placement" assumes the seller wants a
known buyer. Sellers sometimes prefer a block precisely because it spreads stock across many holders and
avoids creating a new controlling one.

**Links:** [[canon-akerlof-market-for-lemons]] (why buyers demand a discount from an informed seller) ·
[[wss-trading-hedge-funds]] · [[wss-rates-macro]] (DV01)

---

## 11 · SPACs, SPARCs and listed cash vehicles

**What it is.** A SPAC (special purpose acquisition company) IPOs as an empty shell, puts the cash in
trust, and has 18–24 months to merge with a private company. The merger takes the private company
public. A SPARC (Ackman's variant) collects only *rights*, and holders fund once a target is named.
Investors in either are buying the sponsor's judgment, a blind pool.

**How it works** (Chamath's 2025 American Exceptionalism Acquisition Corp, from the S-1 as read on air):
- 25M class A shares × $10 = **$250M** in trust.
- Sponsor paid **$25,000 for ~12M class B founder shares** (~$0.002/share). 12/(25+12) ≈ **32%**, the
  "promote" (classic SPACs: ~20%). New in this vintage, the promote vests on hurdles: 1/3 at $15 (+50%),
  1/3 at $17.50, 1/3 at $20, each over 20 of 30 trading days post-merger, all vesting on change of control.
- **Fees hit twice:** underwriting of 30 cents per $10 unit (**3%**) on the shell, then merger fees.
  Kristen's "35% in fees" adds the ~3% underwriting to the ~30% promote plus merger costs. Strictly the
  promote is dilution, not a fee, and it is now contingent on the stock rising 50–100%.
- **Units with warrants are gone.** Old units were 1 share + a warrant fraction (strike ~$11.50). *SPAC arb*
  funds bought units near NAV, redeemed or sold shares at the vote, and kept the warrants as a free option.
- Target ≈ **4–5x the trust**, so a $250M SPAC buys a $1–1.5B company. The other ~80% of the financing is
  **rollover equity** from the target's existing holders plus a private placement raised once the target
  is known (Myers). The end state looks like an IPO with ~20% float.
- **A cousin: the listed closed-end fund.** Ackman's Pershing Square USA (2024) aimed to raise $25B,
  cut to $2.5–4B, then pulled. Kristen's pricing point: a fund that is a pile of cash is worth at most the
  cash raised, and less after underwriting fees. There is no growth story to justify an IPO premium.

**Business significance.** Sponsors capture the promote. The target gets listed without an IPO bookbuild
(WeWork, after its failed 2019 IPO). Early retail buyers get exposure to private companies. Myers: few
large banks underwrite SPACs now; smaller boutiques specialize in them.

**Forces and impact.** Kristen and Jen tie both SPAC mania and meme stocks to **zero rates**: cash
"had to go somewhere." SPACs from 2020–21 trade down 65–90% (short) or 60–95% for Chamath's names (Virgin
Galactic, Opendoor, Clover; SoFi the exception at ~$22.75). Early 30–50-day pops gave way to poor
long-term performance. The 2025 return of SPACs coincides with expected easing. Bok's career observation:
in 2021 everyone wished they were "a SPAC person"; the ladder then dropped.

**With vs. without.** Without SPACs, weak companies must survive a bookbuild. With them, the
sponsor's promote and double fees are a dilution tax on public holders. Kristen's verdict: closer to a
scam than an investment. Jen's comparison: the meme-stock version of private equity.

**Applies when:** liquidity-flush markets, retail demand for private names. **Breaks when:** rates
rise and redemptions drain the trust; when the 30-day hurdle is too short to prove anything.

**Channel example.** "Chamath's New SPAC (Detailed Breakdown)"; "The HIDDEN Cost of SPACs"; "Panic (!) in
the Markets, Ackman's Canceled IPO"; "The INSANE Loophole GameStop could use…" (SPAC → SPARC → GameStop lineage).

**Counterpoint.** The hosts lump all SPACs together. A few (e.g. DraftKings, SoFi) worked, and the 2022 SEC
rules plus hurdled promotes partly fix the incentive problem. Myers's kinder framing: a SPAC lets a proven
operator raise a war chest for the next company. Kristen's own point stands: a 30-day hurdle is easy to
pump. A fairer benchmark Jen raises but doesn't run: SPAC vs. search-fund returns (§19).

**Links:** [[canon-jensen-meckling-agency-theory]] (sponsor/shareholder conflict) · [[tiger-sisters-wealth-mechanics]]

---

## 12 · Cash vs. stock consideration, and collars

**What it is.** A buyer can pay the seller's shareholders in cash, its own stock, or a mix. Stock
introduces price risk between signing and closing, often a year. A *collar* splits that risk:
inside a price band the seller gets a fixed *value*; outside it the seller gets a fixed *number of shares*.

**How it works** (Netflix / WBD, signed Dec 5, 2025):
- Offer: **$27.75 = $23.25 cash + $4.50 of Netflix stock.**
- The two interests the collar reconciles (Kristen): the seller wants the promised $27.75 even if Netflix
  falls; the buyer cares how many new shares it must issue, because more shares mean more dilution.
- Collar: if Netflix's 15-day VWAP before close is between ~**$97.91 and ~$119**, the exchange ratio
  floats to deliver exactly $4.50. Below $97.91 the ratio fixes at **0.046** (4.50/97.91). Above ~$119 it
  fixes at ~0.0376. The transcripts say "0.376" and "0.46", which are caption slips.
- What happened: Netflix fell from $103.22 (signing) to ~$88 → 0.046 × 88 = **$4.05**, so the offer was
  really **$27.30**. At $85, the stock leg was $3.91.
- Netflix's fix: switch to **all cash at $27.75**. That removes uncertainty, speeds the shareholder vote, and
  takes away Paramount's argument.
- **Private buyers.** Mars, privately owned, paid **all cash, $35.9B**, for Kellanova (2024). A private
  company *can* pay in stock (Facebook bought Instagram in 2012, before its own IPO, with a cash-and-stock
  mix), but sellers then hold an illiquid, unpriced currency, so cash dominates.
- The tax angle for sellers: cash is taxable at close. Stock (and a qualifying tax-free spin) can defer.

**Business significance.** Sellers care about *value*; buyers care about *share count* (dilution).
A collar is a negotiated settlement between those two interests. Jen's rates translation: it is like a
costless swaption collar. A non-costless version is a risk reversal.

**Forces and impact.** Stock consideration works when the buyer's stock is strong. As Netflix's market cap
fell (by more than WBD's value), stock became a weak currency and the collar floor shifted risk
back to WBD holders. Second-order effect: switching to cash required debt and **pausing buybacks**, which
the market disliked (§13).

**With vs. without.** No collar: sellers bear all buyer-stock risk (or buyers bear unlimited
dilution under fixed value). All cash: certainty for sellers, but leverage and EPS cost for the buyer.

**Applies when:** long sign-to-close periods with regulatory review. **Breaks when:** the buyer's stock
moves outside the band; when stock is the buyer's "Monopoly money" (GameStop, §17).

**Channel example.** "Netflix / WBD $83bn Deal: Breaking Down This One Critical Detail"; "The truth behind
why Netflix is changing their WBD bid"; "Netflix to pay ALL CASH for Warner Bros. Why the stock price
tanked"; "Investment Banking Hours, Mars Deal, & Google Monopoly."

**Counterpoint.** The hosts treat the switch as defensive tidying. It was also a signal: Netflix
preferred to lever up rather than issue stock at $88, which can be read as management thinking its stock
was cheap. Kristen's suggested interview question ("why was Mars all cash?") has a simpler answer than it
looks: no listed currency, and a family owner that won't dilute.

**Links:** [[market-structure-24-5-trading]] (VWAP collars hang off closing prices) ·
[[canon-dixit-nalebuff-thinking-strategically]]

---

## 13 · Accretion/dilution and relative P/E: the affordability test

**What it is.** Accretion/dilution asks whether the buyer's EPS is higher or lower after the deal:
(buyer NI + target NI + synergies − financing cost) ÷ post-deal shares. *Relative P/E* shortcuts
which payment currency is cheaper.

**How it works:**
- **Cost of each currency** (Netflix at ~37x P/E):
  - Stock: 1/P/E = 1/37 ≈ **2.7%** of earnings yield given up.
  - Debt: 5.5% × (1 − 25% tax) = **4.125%** after tax. The transcript says 4.215%, an arithmetic slip.
    Its "P/E of debt" is 1/0.04125 ≈ **24x**.
  - Higher P/E is the cheaper currency. Stock (37x) beats debt (24x), so switching to all cash made the
    deal *more dilutive*. That is the hosts' explanation for Netflix's drop on the switch and on earnings
    (EPS $0.56 vs. $0.55 est., revenue $12.05B vs. $11.97B, +18% y/y, stock still −6%).
- **Cash on hand isn't free** (Google / Wiz, $32B all-cash): forgone interest $32B × 5% = $1.6B pre-tax ≈
  **$1.2B after tax**. Wiz revenue ~$500M (2024) → ~$1B (2025E). At a generous 20% margin, that's ~$200M NI, a
  **~$1B annual EPS hole**. Only revenue synergies could close it. Markets discount those, so the stock fell ~2.5%.
- **Purchase accounting** distorts this: acquired assets are written up to fair value and then amortized,
  which depresses reported target earnings. Part of WBD's poor expected earnings is amortization
  "hangover" from the AT&T and Discovery deals.
- **High-P/E acquirer vs. low-P/E target:** GameStop at ~34x vs. eBay at ~24x (CapIQ). A high-multiple buyer
  issuing stock for a low-multiple target is mechanically accretive. Kristen's caveat: equity "trading like
  Monopoly money" is accretive *because* it's overvalued.
- **Paying up:** Mars paid ~17–18x EBITDA for Wrigley in 2008 when confectionery comps traded ~10–12x
  (Kristen, from *The Chocolate Wars*). A private buyer has no EPS to dilute and can pay for strategy.

**Business significance.** Strategic acquirers' boards and shareholders judge deals here, because stocks
trade on expected EPS. Private equity judges on IRR (20–25% targets) instead. That is why PE won't pay
~17x EV/EBITDA for eBay to lever at 6–7x without growth.

**Forces and impact.** Rates set the cost of debt and of forgone interest. P/E levels set the cost of stock.
When rates rise, cash deals get more dilutive. When multiples are rich, stock deals win. Revenue
synergies are discounted, cost synergies credited. Kristen: "you never want to be a synergy," since
synergies mean layoffs (~$6B/yr expected at WBD).

**With vs. without.** Without this test, managers buy growth at any price (empire-building). Leaning
on it too hard means rejecting strategic deals that are dilutive for years but valuable (Amazon paid all
cash for Whole Foods and One Medical although stock was the more accretive currency).

**Applies when:** strategic buyer, public currency. **Breaks when:** the deal is existential, not
optional (Paramount), or the buyer's P/E is a bubble.

**Channel example.** "M&A Math that Forced Netflix to Walk Away From Paramount"; "Why Google did a
$32Bn acquisition when they knew it would tank their share price."

**Counterpoint.** Kristen says it cleanly herself: **accretion/dilution is an affordability test, not
a valuation.** A deal can be accretive and value-destroying (overvalued stock buying a cheap
target), or dilutive and value-creating. EPS-targeting is exactly what Bezos's letters argue against
([[canon-bezos-shareholder-letters]]). The Logan Roy line from *Succession* sums up the gap:
"congratulations on saying the largest number." Being able to pay a price is a separate question from
whether to pay it.

**Links:** [[canon-bezos-shareholder-letters]] · [[canon-munger-poor-charlies-almanack]] (incentives) ·
[Unit 06](../learn/unit-06-whats-a-business-worth.md)

---

## 14 · Sources and uses, financing commitments, leverage capacity

**What it is.** Every acquisition has a *uses* side (equity purchase price, refinancing target debt,
fees) and a *sources* side (cash, new debt, new equity) that must balance. Debt is sized as a multiple
of EBITDA. A **commitment letter** is a bank's (conditional) promise to lend.

**How it works:**
- **Private vs. public target.** Buying a private company is usually **cash-free, debt-free**: the buyer
  pays for the whole house, the seller pays off its own mortgage and keeps the safe in the living room.
  Uses = enterprise value + transaction fees + financing fees + the **minimum cash** the business needs to
  operate. Buying a public company, you buy every share (at a premium), refinance the debt, and pay fees;
  the target's cash comes with the equity, so its **excess cash** (above, say, $10–25M) appears as a
  *source* (CFDF short).
- **Change-of-control clauses.** Only debt whose documents require repayment on a change of control (or
  above a leverage trigger) must be refinanced. Paramount didn't need to refinance all of WBD's debt,
  but did need to refinance most.
- **Paramount for WBD (hostile, $30 version):**
  - Uses: equity $72B + refinance WBD debt $35B + breakup fee $2.5B ≈ **$110B**.
  - Sources: **$54B committed debt** (BofA, Citi, Apollo) + **$56B equity** ($15B existing PSKY equity
    rolled in + $24B Gulf sovereign funds and Kushner's Affinity Partners + **$17B Larry Ellison backstop**
    with RedBird) = $110B. Headlines quoted "$41B from Ellison and RedBird", which bundles the backstop
    with others' money.
  - Leverage ~5.5x pro forma. Later analysis on an LTM basis: **6.5–7x** on a ~$110–111B EV, the largest
    LBO ever. EA's $55B LBO (Silver Lake, PIF, Affinity; $20B JPMorgan commitment) was the prior record.
  - Paramount was worth ~$29B in total, only ~$15B of it equity, and already ~5.5x levered. Kristen's
    point: "Paramount was almost inconsequential." Buying WBD's EBITDA actually improves Paramount's own
    leverage ratio. The deal is a leveraged buyout with a strategic as the vehicle.
  - **Thresholds Kristen uses:** steady businesses lose investment grade around **3.75–4x** debt/EBITDA;
    ~5.5x is classic LBO territory; ~6x is the regulators' line (the post-2008 leveraged lending guidance;
    see [[wss-credit-distressed]] for the caveats).
  - **The $40B personal guarantee.** After Affinity walked, WBD's board asked why Ellison couldn't
    personally backstop the equity the way Musk did for Twitter. Ellison then guaranteed ~$40B, without
    raising the price. Kristen's read: certainty without more money doesn't beat a signed deal with a
    better-capitalized buyer, so expect a price bump (she floated up to ~$34). It came, at $31 (§15).
    Oracle's stock slide had cut Ellison's net worth by ~$25B in a day, which is why the board asked.
- **GameStop for eBay ($56B, half cash):**
  - Cash: $28B needed = $9B on hand + **TD Bank letter for "up to" $20B**.
  - Pro forma debt ≈ $4B GME + $7.2B eBay + $20B new ≈ **$31B**. EBITDA ≈ $0.3B GME + $2.7B eBay ≈ $3.0B,
    so **~10x**. "Massively levered" LBOs are ~7x. Kristen says banks simply do not lend at 10x.
  - Stock: $28B needed vs. an $11B market cap, a ~$17B hole. "Just raise more equity" doesn't work:
    issuing shares into an $11B company leaves an $11B company with more shares.
- **LTM vs. forward:** lenders underwrite on last-twelve-months EBITDA without synergies ("what have you
  done for me lately?"). Equity investors price on forward expectations. Paramount's press release quoted
  pro forma, synergized forward leverage. Lenders don't use that measure.

**Business significance.** Sources and uses is how you test whether a bid is real. Who supplies the equity
also determines who controls the company afterwards (§17).

**Forces and impact.** Cheap, plentiful private credit (Apollo) and sovereign wealth make mega-LBOs possible.
Second-order effect: an existential bidder with a deep-pocketed backstop can outbid a disciplined strategic
buyer, leaving the *target* with the leverage. The hosts estimate a 30–35% 3–5-year bankruptcy risk at
GameStop/eBay leverage. Caesars (2008 Apollo/TPG LBO) is the case: the thesis was right, the equity was
still wiped out.

**With vs. without.** Without commitment letters, sellers can't judge certainty. With soft ones ("up to"),
they can't either. A small acquirer without a backstop has no credible bid. That is the hosts' whole case
that GameStop "isn't Paramount": Ryan Cohen is worth ~$5B; Larry Ellison ~$200B+.

**Applies when:** any levered deal. **Breaks when:** sponsors announce first and look for equity later.
Jen's objection: you line up partners *before* you post the bid on your website.

**Channel example.** "Breaking Down Paramount's $108bn Hostile Bid for Warner Brothers Discovery"; "Larry
Ellison just guaranteed $40B"; "Cash Free Debt Free EXPLAINED"; "GameStop just bid $56 billion for eBay";
"GameStop's bid for eBay: breaking down the insane math."

**Counterpoint.** The hosts lean on leverage ratios as hard limits. In practice lenders will stretch for
asset-rich or forward-growing credits. Kristen concedes TD may be using next year's EBITDA, which would make
it ~7x rather than 10x. Kristen also admits that in a season-one *Succession* episode she called a $100B
hostile LBO unrealistic; Paramount did one.

**Links:** [[tiger-sisters-private-capital-101]] (Toys R Us: leverage as the house-burner) ·
[[wss-credit-distressed]] · [[canon-taleb-antifragile]]

---

## 15 · Contested deals: auctions, hostile bids, deal protection, Revlon

**What it is.** When a target is in play, the board can negotiate privately, run a formal auction,
or face a *hostile* bidder who goes directly to shareholders (a tender offer needing >50%). Contracts
carry *protections* (breakup fees, reverse termination fees, ticking fees). In a sale of control,
Delaware's **Revlon duties** require the board to maximize the price shareholders get.

**How it works** (WBD timeline as relayed):
- WBD listed Apr 2022 at $24; low ~$7.52 (it was ~$7 in April 2025); ~$12.54 when Paramount approached
  (Sept 2025).
- Paramount bids **$19** (cash/stock) → rejected; **$22** + breakup fee → rejected; **$23.50**, 80% cash → rejected.
- Zaslav runs a **formal auction** (Paramount, Netflix, Comcast). Kristen's analogy: bringing in a
  real-estate agent instead of taking the first knock on the door.
- Final bids Dec 5: Netflix **$27.75** for studios + streaming only. Paramount **$30** for everything.
  Board signs Netflix, valuing its package (including the spun cable assets, §16) at ~**$31–32**.
- Paramount goes hostile at $30, sues, then (Feb 2026, after Netflix lets WBD talk) raises to **$31**.
  It also agrees to pay WBD's **$2B breakup fee to Netflix**, a **$7B reverse termination fee** if regulators
  block the deal, and a **ticking fee of $0.25/share per quarter** past the deadline (≈$650M/quarter on
  ~2.5B shares).
- Netflix declines to match; its stock *rises* on walking away, and it collects the $2B.
- **Why a co-investor walked.** Kushner's Affinity Partners left the Paramount equity group. Kristen's
  explanation is money, not politics. Strategic investors buy for operating reasons (easier to buy HBO
  than build it). Financial investors buy to sell at a return. Sovereign funds can accept low returns for
  influence and positioning (PIF's rumored ~$800M for Tiger Woods to join LIV Golf). Affinity's LPs
  overlap with those sovereigns, but Affinity itself is paid PE-style, management fee plus carry on deal
  returns. Every price bump lowered its expected IRR until the math stopped working.

**Business significance.** Auctions convert a buyer's *need* into price. Breakup fees compensate the
jilted bidder's costs. Reverse fees and ticking fees put a price on regulatory and timing risk. Revlon
explains why WBD's board took a deal that may be bad for WBD the *company* (heavy leverage): in a cash
change of control, shareholders get paid and leave.

**Forces and impact.** Regulatory odds became part of the bid. The hosts point to perceived political
proximity (Ellison–Trump) and "smear campaigns" over which bidder could close. Change-of-control payouts
follow: **Zaslav ~$887M**, of which ~**$335M is a golden-parachute tax gross-up**. The 20% excise tax
(IRC §280G) applies when a payout is ≥3x the base amount. Reimbursing it is itself taxable, so it circles
up from ~$100–150M to $335M. Kristen says the "312% premium" headline is measured off the $7.52 low. Off
the ~$12.54 undisturbed price, $31 is ~147%.

**With vs. without.** No auction: the first bidder sets the price ($19). No breakup fee: no bidder spends
months on diligence. No Revlon: boards could pick the bidder they like over the one that pays most.

**Applies when:** strategic scarcity (a library that makes Paramount "a real player"). **Breaks when:**
the winner overpays (the "cursed asset" history: AOL–Time Warner destroyed ~$100B; AT&T paid $85B equity /
$108B EV in 2016, then spun Warner Media out via a reverse Morris Trust in 2021).

**Adjacent tactics from the cluster:** a **headline anchor bid** (United floating American as a ruse to
make a JetBlue bid look modest, per the "conspiracy" theory); a **toehold via derivatives**
(GameStop's reported ~5% eBay stake; the Porsche/VW cash-to-physical-settlement switch that later
prompted disclosure rules); **antitrust breakups** (Adobe paid Figma a **$1B** breakup fee when EU
regulators blocked its $20B deal; JetBlue/Spirit was blocked and Spirit is now heading for liquidation
anyway). **Terminology:** commentators called Paramount/WBD a "reverse merger" because the smaller company
buys the bigger. Kristen and Jen conclude it isn't one: a reverse merger is a private company buying a
listed one to go public without an IPO, SPAC-style.

**Channel example.** "M&A Math that Forced Netflix to Walk Away From Paramount"; "Paramount update: the
media's not talking about THIS REASON Jared Kushner's PE firm walked from WBD"; "Warner Bros CEO pay
close to $1 billion"; "Why Paramount's $30.00 bid for WBD is worse than Netflix's $27.75."

**Counterpoint.** The hosts frame Paramount as irrational ("doesn't play by the rules"). A buyer for
whom the asset is existential has a rational higher reservation price, and the auction extracted it.
Whether *Paramount* created value is a separate question from whether *WBD holders* did. On Affinity,
"it was the IRR" and "it was politics" aren't exclusive. Kristen allows both.

**Links:** [[canon-schelling-strategy-of-conflict]] (commitment, anchors) · [[canon-dixit-nalebuff-thinking-strategically]] ·
[acumen case 04 — Disney](../acumen/case-04-disney.md) (same streaming-library war, strategy side)

---

## 16 · Spin-offs, split-offs and separation structures

**What it is.** A company can break up by *selling* a division (a divestiture) or by *separating* it
in the public market. In a **spin-off** it distributes the subsidiary's shares to existing holders pro
rata, so everyone owns both pieces. In a **split-off** holders *choose* whether to exchange parent shares
for subsidiary shares. An **equity carve-out** sells part of the subsidiary in an IPO. Value is split,
not created: one $23 stock becomes, say, $4 of cable + $20 of studio. Spins can be tax-free if they meet
IRS requirements, and often precede or enable a sale.

**How it works:**
- **Spin-off, worked (Kellogg, Oct 2023).** Holders got **1 share of WK Kellogg (cereal) per 4 Kellogg
  shares**, tax-free. The remaining snacks company (Pringles, Cheez-It) renamed itself **Kellanova**,
  which Mars agreed to buy for **$35.9B all cash** in Aug 2024. The spin turned one conglomerate into a
  sellable snack pure-play.
- **Split-off, worked (hypothetical Instagram, from Meta).** Zuckerberg reportedly considered a spin of
  Instagram in 2018 under antitrust pressure. A sale wouldn't work: at $100B+ only another tech giant
  could pay, recreating the monopoly problem. In a split-off, Meta holders who want Instagram hand in Meta
  shares to get it. Two separate investor bases result, and **Meta's share count falls, so it works like
  a buyback**.
- **Netflix's structure:** WBD spins off its cable networks (CNN, TNT, TBS, Discovery) to shareholders.
  Netflix buys only studios + streaming (HBO, HBO Max, WB film/TV, library).
- **Apples to apples:** Paramount's $30 for everything vs. Netflix's $27.75 for part. The gap
  ($2.25) is what Paramount implicitly assigns the cable assets. Kristen's check: cable EBITDA ~$6–7B ×
  a conservative 4x ≈ $24–28B, less ~$18.5B of debt assigned to SpinCo ≈ $5.5–9.5B ÷ ~2.4–2.5B shares ≈
  **$2.20–3.90/share**. She says "$3.50–4," the top of that range. Other estimates she cites: Paramount
  ~**$1**, a BofA analyst ~**$5**, and a joke that you'd pay someone to take it (negative). Board's own
  number for the Netflix package: ~$31–32.
- **SpinCo leverage.** Debt follows the assets. The declining cable SpinCo inherits a large share of
  WBD's debt and could become distressed on its own, which is why its value is so contested.
- **Precedents:** Disney / 21st Century Fox (2019). New Fox was spun out and Disney bought the rest.
  AT&T / Warner Media → Discovery via a **reverse Morris Trust** (2021), where a spin is merged tax-free
  with another company.
- **Low headline premium:** Netflix's $27.75 looked like only ~10–15% over a ~$23–24 price. Partly because
  the stock already priced in the bidding war, mostly because the market price reflected *all* assets
  while Netflix bought only some.

**Business significance.** Separation lets a buyer take only what it wants, closes a **conglomerate
discount** (Kristen's explanation: opacity gets penalized; separated companies tend to perform better),
and gives shareholders a choice. Tax-free status is often the deciding constraint.

**Forces and impact.** Antitrust pressure (Meta, Google) and activist pressure push separations.
Declining-but-cash-generative assets (cable, cereal) trade at very low multiples, so the bidder buying the
whole company captures them cheaply unless the seller spins them first. Second-order effect: the leftover
SpinCo is a "sitting duck" for another buyer, so CNN wasn't safe under either outcome.

**With vs. without.** Without spin-offs, a buyer for half a company has to buy all of it or walk.
Without split-offs, a forced breakup can't let holders sort themselves into the piece they want.
Bidders aren't comparable without a SpinCo valuation, which is exactly the fight Paramount took to court.

**Applies when:** parts have different natural owners. **Breaks when:** SpinCo is overloaded with
debt (common), or the spin fails tax-free tests and the "value" becomes a tax bill.

**Channel example.** "Big Tech Breakups: How a Spin Off or Split Off of Instagram from Meta Would Work";
"Investment Banking Hours, Mars Deal, & Google Monopoly"; "Breaking Down the Netflix / Warner Brothers $83bn
M&A Deal"; "Why Paramount's $30.00 bid for WBD is worse than Netflix's $27.75."

**Counterpoint.** "Separated companies outperform" is partly selection: firms spin out pieces when they
expect them to do well, and studies disagree on how durable the effect is. Forced breakups are costly:
Kristen's Microsoft history (a 2000 breakup order, overturned on appeal and settled) included a ~55%
share-price fall over the next year and years of distraction. The hosts' SpinCo math leans favorable to
the Netflix side; market multiples for declining linear TV have been below 4x at times.

**Links:** [acumen case 04 — Disney](../acumen/case-04-disney.md)

---

## 17 · Rollover equity, and ownership vs. control

**What it is.** *Rollover equity* is when sellers take stock in the new combined or private company
instead of cash. That is standard for management in LBOs, and the main financing in SPACs. *Ownership
vs. control*: economic ownership (share of profits) and voting control can be separated with dual-class
shares.

**How it works:**
- **Skechers / 3G Capital (2025, ~$9B take-private).** Holders could elect **$63 cash**, or **$57 cash plus
  one private "equity unit"** in the new company. Rollover was **capped at 20%** so 3G keeps at least 80%.
  The election prices the unit: a holder who rolls gives up $6 of cash for it, so the cash-equivalent
  value implied for one unit is $6. Why offer it: a holder sitting on a ~20% loss amid tariff fears can
  sell now and still share any recovery. Kristen's analogy is selling your house to a flipper for less in
  exchange for a cut of the resale. Management, meanwhile, gets to fix the business away from quarterly
  scrutiny.
- **GameStop / eBay, re-presented the next day.** The house analogy: your neighbor offers $1M for your $1M
  house as $150k cash + $350k borrowed *against your house* + $500k of equity in the combined property
  (your house + their $100k house), which also sits in a hurricane zone. Mapped to the deal:
  - cash mostly from **eBay's own debt capacity**
  - stock in the *combined* entity, not GME shares, so the equity mostly comes from **eBay holders rolling over**
  - pro forma ownership **~40% GME / 60% eBay**, for only a ~25% premium
  - eBay holders could take that cash themselves with a **dividend recap**, without GameStop
  - Kristen's better version: all-stock, low leverage. Because GME trades at 34x vs. eBay's 24x, a
    **contribution analysis** (who brings what sales and EBITDA) means eBay effectively gets a control
    premium *paid to it*. She jokes that it's like being asked out and then having to pay for dinner.
- **Ackman's UMG SPARC:** the headline said a "$64B takeover." In substance it was ~$2.5B to lift his stake
  from ~7% to ~11%, dressed up by rollover mechanics.
- **Control:** Paramount Skydance post-deal economics would be PSKY holders 27%, sovereigns/Affinity 43%,
  and Ellison ~30%. But the Ellisons bought Shari Redstone's voting class A shares and the remaining control
  shares, so they hold **100% of the vote**. Public PSKY holders go from 0% to 0% control. Foreign investors
  would take non-voting shares to satisfy US rules. **Alphabet** has class A (1 vote, GOOGL), class C
  (0 votes, GOOG), and privately held class B (10 votes). C was created so that issuance for M&A and stock
  comp wouldn't dilute founder votes. **SpaceX:** Musk keeps majority control below 50% economics.

**Business significance.** Rollover aligns sellers with the outcome and stretches a buyer's purchasing
power. It also lets a small acquirer claim a "takeover" mostly paid for by the target. Dual-class lets
founders raise capital without giving up decisions.

**Forces and impact.** Kristen dates the shift from cash takeovers to rollover-funded "takeovers" to SPACs.
Volatile markets (tariffs, in Skechers' case) make an election attractive: holders who disagree on value
can sort themselves into cash or upside. Second-order effect: headline deal values stop meaning what
readers assume. Governance concern: non-voting money can still buy influence through back channels.

**With vs. without.** All-cash: clean exit and full price discovery. Heavy rollover at high leverage:
sellers keep risk but lose control. Kristen's point for eBay holders is that they gain a lot more risk
without being paid for it. Skechers shows the opposite design: capped, optional, and priced.

**Applies when:** sellers believe in the combined upside (management, SPAC targets, contrarian public
holders). **Breaks when:** rollover is paired with LBO-level leverage and no liquidity. A private unit
can't be sold, so the holder's exit depends entirely on the sponsor's timetable.

**Channel example.** "Skechers' $9B deal shows why in LBOs, cash isn't always king... A Primer on Rollover
Equity"; "The INSANE Loophole GameStop Could Use to Pull Off Buying eBay (4x its size)"; "Who will control
CNN / HBO if Paramount buys WBD?"

**Counterpoint.** The hosts' "you never want to own the levered combined equity" ignores that this is
exactly what PE rollover founders do, sometimes very profitably. The difference is who operates and
how fast debt is paid down. Skechers is the cleaner test of their view. The cap and the $6 haircut mean
3G decides how much upside it shares, and the minority unit has no vote on when 3G exits.

**Links:** [[canon-jensen-meckling-agency-theory]] · [[tiger-sisters-private-capital-101]]

---

## 18 · Biotech capital markets: probability-weighted DCF and the equity-only life cycle

**What it is.** Most small biotechs have no revenue for 5–10 years. They are valued by forecasting a drug's
sales to patent expiry, then multiplying each year by the *probability of success* (risk-adjusted
NPV, rNPV). They fund themselves almost entirely with equity, raised at clinical milestones.

**How it works** (Sonia Gupta, Goldman):
- Comps fail because there are no earnings or revenue to multiply. The **DCF runs 20–25 years** to patent expiry.
- Revenue = patients × price, but each patient count is itself a model: prevalence × diagnosable × access to
  a test × competitive share in a landscape 10 years out.
- **Probability of success:** roughly 10% of drugs moving from animal testing into humans reach approval (a
  "massive generalization"). Adjusted revenue = unadjusted × PoS. It steps up after each trial readout and
  reaches 100% at launch.
- **WACC by stage:** a single rate for a given valuation date, but lower for late-stage peers than early-stage.
  Big pharma's is often about half of biotech's. Recent volatility has raised WACC and cut fundamental values.
- **Financing path:** private rounds → IPO (historically phase 2; in 2020–21 even preclinical/phase 1,
  ~75 IPOs >$50M each year) → **follow-ons at inflection points** (a readout de-risks, stock jumps,
  company raises) → eventually acquired by pharma, which uses biotech as an external R&D arm.
- When markets are shut: reverse-merge into a cash-rich shell with a failed drug, sell the lead asset and
  spin early programs back into private hands. Defense work is a big share of the job because
  public prices often sit far below insiders' fundamental view.

**Business significance.** This is the one sector that still IPOs pre-profit. Pharma relies on it to refill
pipelines. Bankers act partly as investors, screening management, capital discipline and science.

**Forces and impact.** **The XBI biotech index trades inversely to rates.** Long-duration, cash-burning,
equity-only companies are the extreme case of rate sensitivity. Second-order effect: the Feb 2021 biotech
crash came right after the vaccine success, because rate expectations moved. Policy (NIH and university
funding cuts, FDA shifts toward in-silico testing) adds uncertainty to the timelines. Rare-disease drugs
below ~$500M peak sales often don't clear big pharma's hurdle, so creative structures keep them alive.

**With vs. without.** Without probability weighting, every pipeline looks either worthless (no revenue) or
priceless (peak sales). Without a public window, biotechs merge, license or shut down.

**Applies when:** binary, milestone-driven assets. **Breaks when:** PoS base rates don't fit a novel
modality, or when a 25-year forecast is tuned to justify a raise.

**Channel example.** "Biotech Investment Banking 101 feat. Goldman Sachs' Sonia Gupta."

**Counterpoint.** The guest is a recruiter for her firm and her sector. The interview has no discussion of
how often bankers' rNPVs prove right, or of fee incentives to time follow-ons at stock peaks. Her "~10%" is
close to published phase 1→approval rates (~8–12%) but varies widely by therapeutic area.

**Links:** [[canon-tetlock-superforecasting]] (base rates) · [[canon-mauboussin-success-equation]]

---

## 19 · Small-deal acquisition financing: entrepreneurship through acquisition (ETA)

**What it is.** Buying an existing small business to run it, instead of starting one. It is financed with
some mix of personal or raised equity, SBA or bank debt, and seller notes. It comes in two models: a
**search fund** (investors pay the searcher's salary, then fund the deal) or **self-funded** (searcher pays
their own way and owns the equity).

**How it works** (Jesse Sapphire, ABG Print, bought June 2019; EBITDA ~$1.3–1.5M):
- **Scale ladder:** seller's discretionary earnings (SDE: EBITDA plus owner pay and perks) $0–1M = "anybody
  buying anything" (laundromats, bars). Self-funded searchers buy at ~$0.5–3/4M EBITDA. Search funds buy
  bigger. Lower-middle-market PE starts around $5M. Below that, PE associate time costs more than the deal
  supports, unless the target is a tuck-in.
- **Search-fund economics:** search capital gets a step-up multiple when it rolls into the deal. The searcher
  typically gets ~25% of the gain over cost plus a hurdle at exit, with no equity of their own. So searchers
  want *high-growth* targets (home health staffing, SaaS) and *big* deals. A slow, single-digit-growth
  business creates value mainly through debt paydown, which doesn't suit the model. Stanford data: ~75% of
  searchers close a deal.
- **Debt stack:** SBA loans (10-year term; personal guarantee required from any owner >20%, a non-starter for
  fund investors) or conventional bank debt (7 years). His borrowing rate was ~11.5%. These are cash-flow
  "airball" loans with no hard collateral.
- **Seller note** (example: $10M price = $6M bank + $2M buyer equity + **$2M seller note**): second lien,
  fixed rate, sometimes on standby until senior debt is paid, and sometimes *forgivable* on missed targets,
  replacing an earnout. Banks treat seller paper almost as equity, because it signals the seller believes in
  the business and keeps the seller engaged through the transition. The broker adage he cites: "you want
  liquidity or you want price?" (Skechers' cash-or-unit election, §17, is the public-market version.)
- **Structure:** asset purchase (no inherited liabilities, stepped-up tax basis) vs. stock purchase (inherits
  history). He used a **§338(h)(10)** election, a stock deal taxed as an asset deal.
- **Why deals die** (rarely price): business changes mid-process, hidden concentration (top five clients
  routed through one referrer), indemnity.
- **Permanent capital vs. a 3–7-year exit:** revenue fell **95%** in March 2020 and staff went from 24 to 4.
  A fund-backed owner would have shut it. As permanent capital, he drew the full credit line (copying
  Boeing), took two PPP rounds, repositioned from ~90% financial-services clients to ~40%, and passed 2019
  revenue in 2024.

**Business significance.** This is the succession gap: aging owners and no heirs, sold through brokers who
charge ~10%. The buyer is "the worst kind of buyer" (no money, no industry experience, risky to lend to), so
the targets have flaws that PE passed on.

**Forces and impact.** Rates drive SBA and bank cost. Fund time horizons force exits at bad moments.
Second-order effect: the model selects for operators good at the mundane over strategists. In the guest's
example from the search-fund world, a snowplow business was losing a third of its orders because the
afternoon Wi-Fi kept failing. His "90-day amnesty on problems" was the actual turnaround plan.

**With vs. without.** Without seller financing and SBA, the self-funded model barely exists (bank
LTVs alone won't cover the price). Without permanent capital, cyclical shocks force sales at the bottom.

**Applies when:** stable, explainable, "cockroach" businesses (profitable every year since 1992, survived
9/11 and 2008). **Breaks when:** the hidden concentration materializes (in-person NYC economic activity, in
his case).

**Channel example.** "Entrepreneurship Through Acquisition 101" (with Jesse Sapphire).

**Counterpoint.** Survivorship: the guest is a success story narrating his own deal, and he hints at the luck
involved (PPP "bailed me out"). His claim that W-2 jobs are riskier than owning a business is fair on
correlated career risk. It understates how concentrated an owner's wealth becomes. The hosts' search-fund
economics differ from Codie Sanchez's in [[tiger-sisters-wealth-mechanics]]: investors take 50–70% there vs.
a ~25% carry-like stake here. Both describe the same thing, investors keep most of the equity, from opposite
sides.

**Links:** [[tiger-sisters-wealth-mechanics]] · [[tiger-sisters-private-capital-101]] ·
[[entrepreneurship-operator-playbook]] · [[canon-taleb-antifragile]] (permanent capital as optionality to survive)

---

## How the concepts connect

```
            WHO DOES THE DEAL (§2): advice-only boutique  vs  bank with a balance sheet
                                         │
                     VALUATION (DCF / comps / rNPV)            ← §1 EV vs equity, §18 biotech
                               │
          ┌────────────────────┴─────────────────────┐
     PRICING (sell a slice)                    AFFORDABILITY (buy the whole)
          │                                          │
 bonds: Treasury + spread, book (§3)      currency choice: cash ↔ stock (§12)
 equity: test-waters → book → discount    cost = 1/PE vs after-tax debt (§13)
 (§4, §5)   or no book at all (§6)                   │
          │                                sources & uses; leverage ≤ ~6–7x LTM (§14)
 greenshoe props price 30d (§7)                      │
          │                                if buyer can't afford → rollover equity /
 tiny float + lockups + index rules (§8)   billionaire backstop / SPAC (§11, §17)
          │                                          │
 unlocks → blocks & follow-ons (§9, §10)   contest: auction → hostile → fees → Revlon (§15)
          │                                          │
 rotation out of substitutes               partial buyer → spin/split decides comparability (§16)
 → single-name vol ↑, dispersion                     │
          │                                          │
 issuers sell what's rich (§9)  ←── rates ──→ cash deals dearer; XBI falls; SPACs die
```

The causal chain worth remembering: **rates up** → forgone interest and debt cost rise → all-cash
deals become more dilutive → strategic buyers prefer stock if their P/E is high → when their stock
falls, collars break and they switch to cash (Netflix) → an existential bidder backed by outside equity
outbids (Paramount), as long as its financial co-investors' IRRs still work (Affinity didn't) → the
target's shareholders get cash, and the target company gets the leverage. On the issuance side, **rich
equity and rich vol** → issuers sell stock and optionality (Google's mandatory, SpaceX's take-it-or-leave-it
price) → a mega-IPO supply wave → passive and active money rotates → index rules get rewritten to absorb it
→ unlocks arrive as blocks. Across both: **the narrower the book, the worse the price discovery** (Figma's
day-one pop, Meta's privately placed SPV bonds, a 42% "block"), and the adviser's business model (§2)
shapes which book gets built.

---

## Retrieval questions

1. **xAI "paid $33B" for X after Musk paid $44B. Did X lose value, and who bore the cost?** Not by EV:
   33 + 12 debt ≈ 45 vs. 44 + 0.6. The cost fell on xAI's outside investors: a 25% stake of an $80B
   company becomes 20/113 ≈ 18% after $33B of new stock.
2. **Why might a company hire a boutique rather than a bulge bracket, and when can't it?** Advice without
   a lender's or trader's conflict. It can't when the deal needs committed financing or underwriting
   (Paramount's $54B of bank debt).
3. **Build the coupon on a new 10-year bond and say what a 3x-oversubscribed book does to it.** Treasury
   yield (5%) + credit spread (1%) = 6%. Excess demand tightens the spread, so the coupon prices lower.
4. **Why is "$135, take it or leave it" unusual for an IPO, and what replaced price discovery?** Normal
   IPOs price off test-the-waters and a bookbuild. SpaceX's demand never set the price. Perpetual
   futures at ~$174 became the coordination point, making the ~20% pop close to self-fulfilling.
5. **Cornerstone vs. anchor: what's the difference and the risk of too much of either?** A cornerstone
   is named on the cover for ~10–20% and may see the S-1 early. An anchor is an expected 5–10% opening
   order with allocation priority. Too much shrinks the float left for everyone else.
6. **Figma popped ~250% but traded at ~$39 five months later. Was it underpriced?** On day one, sellers
   gave up ~$82 × 37M ≈ $3B. Against fair value, $33 ≈ $39 less a 15% discount, so roughly as designed.
   The transfer went to allocated buyers who sold into the frenzy.
7. **What does a company give up by direct listing instead of IPO-ing?** A guaranteed raise and known
   float, coordinated research, stabilization, and the choice of investors. It saves the spread and the
   discount.
8. **Underwriters sold $85B on a $75B deal. What happens if the stock falls vs. rises?** Falls: they
   buy in the market to cover, supporting the price at a profit. Rises: they exercise the 15% greenshoe at
   $135 and the issuer raises ~15% more.
9. **Why sell a 42% stake by private placement rather than a block?** A block of that size can't be
   absorbed without a deep discount, and it hands control to whoever buys. A placement lets the seller
   pick and vet the buyer and negotiate price.
10. **Netflix switched from cash + stock to all cash at the same $27.75. Why did its stock fall?** At
    37x P/E, stock costs ~2.7% of earnings. After-tax debt at 5.5% costs ~4.1% (24x "P/E of debt"). Paying
    cash is more dilutive, and it also meant pausing buybacks.
11. **Below $97.91, what does a WBD holder get for the stock leg, and why?** A fixed 0.046 Netflix shares.
    The collar caps Netflix's dilution, so value falls with the price ($4.05 at $88).
12. **Paramount's $30 for all of WBD vs. Netflix's $27.75 for part. How do you compare them?** Value
    the cable SpinCo holders keep under Netflix. $30 − $27.75 = $2.25 implied for cable. A 4x EBITDA
    SpinCo net of ~$18.5B debt is ~$2–4/share. The board put the Netflix package at ~$31–32.
13. **Why did Kushner's Affinity walk while the sovereign funds stayed?** Affinity is paid on deal-level
    returns; each price bump cut its IRR. Sovereigns can accept lower returns for influence and positioning.
14. **Why does a split-off reduce the parent's share count, and a spin-off doesn't?** In a split-off
    holders surrender parent shares to get the subsidiary (like a buyback). In a spin-off everyone keeps
    their parent shares and receives the subsidiary pro rata.
15. **Skechers holders could take $63 cash or $57 + one unit. What does that imply, and who should roll?**
    The unit is priced at $6 of forgone cash. Holders who think the take-private price undervalues a
    tariff-hit company keep upside; rollover is capped at 20% so 3G controls.
16. **Why does XBI fall when rates rise, and what does that do to a biotech's financing?**
    Long-duration, equity-only, pre-revenue cash flows are the most rate-sensitive. Windows shut, so firms
    wait for readouts, reverse-merge or license.

---

## Gaps (catalog titles relevant to this cluster still without a transcript)

Pass 2 recovered and folded in: JPMorgan ECM 201, Debt Capital Markets 101, Industry S2E3, Elite Boutique
vs. Bulge Bracket, the Paramount hostile-bid episode and its shorts (Ellison guarantee, Affinity walk), the
Netflix collar short, Skechers rollover, Instagram spin/split-off, the xAI "real losers" short, The Hidden
Cost of SPACs, Ackman's canceled IPO, Investment Banking Hours / Mars deal, Cash Free Debt Free. PE
Secondaries 101/201 and LBO in Under 3 Minutes now have transcripts but belong to
[[wss-private-markets-wealth]] and [[tiger-sisters-private-capital-101]]; nothing to add here.

Still missing:
- **S2E2 "Giant Squid" | Block Trades, IPOs vs. Other Equity Offerings** (`beSAafxvKn0`): the episode
  that explains blocks and bought deals directly. §10 is pieced together from S2E3 and the hosts' asides.
- **How Lumi's IPO was Saved By Shady Tricks | Industry S3E2** (`HHHy4hPhDG0`): IPO stabilization and
  book-management abuses.
- **Largest Debt Commitment in History for LBO by ONE BANK. 2008 All Over Again?** (`fZQP_mQ_2sg`): the EA
  financing (JPMorgan's ~$20B) in detail.
- **Paper LBO… IRRs** (`J9xh-sNosSM`): IRR shortcuts behind §13's PE-vs-strategic comparison.
- Possibly relevant: **Industry S3E5 "Company Man"** (`-SWcQh7NJxY`).

Topic gaps even within present transcripts: bought-deal and overnight-block mechanics (discounts, bank
risk, wall-crossing), SPAC PIPE terms, how often direct listings have actually raised primary capital, and
high-yield/leveraged-finance bond issuance (covered only in passing; see [[wss-technicals-career]] for the
LBO financing walk-through).
