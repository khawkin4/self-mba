# Unit 09 — Earning Without Reinvesting: Capital-Light ("Royalty") Businesses

> **For a beginner.** Arc C (the competitive landscape), pairs with Unit 07. New idea: two companies can
> sell the same thing and earn the same profit, yet one is *far* better — because it doesn't have to keep
> sinking money into buildings and equipment to grow. That business keeps more of its cash. This is the
> idea behind what investors call a **"royalty business."**

## Plain words first (read once)
- **Capital expenditure (capex)** — money a company spends on long-lived physical things (buildings,
  ovens, trucks, equipment) to run or grow. It's cash that leaves and becomes an asset, not an expense on
  the income statement.
- **Capital-light (asset-light)** — a business that needs *little* capex to grow, so most of its profit is
  free to return to owners or reinvest in higher-return ways.
- **Capital-heavy (asset-heavy)** — a business that must spend a lot on physical assets just to grow one
  more unit of sales.
- **Franchise / royalty model** — instead of building and owning the stores itself, the company lets
  *franchisees* put up the money to build and run them, and collects a **fee (royalty)** on their sales.
- **Free cash** — the cash left over after the business has paid for the capex it needs. Capital-light
  businesses throw off more of it.

## ① Material — what we're learning
Unit 07 said a **moat** keeps profits high. This unit adds a second axis of quality: **how much capital the
business must consume to earn those profits.** A business that earns a 12% margin while barely spending on
physical assets is worth more than one earning the same margin that must pour cash into buildings every
year — because the first one *keeps* its profit, and the second has to spend it to stand still. The
billionaire investor **Bill Ackman** calls the best version of this a **"royalty business"**: it *"earns a
growing annuity without having to invest much capital."* You can often see it right in the filings.

## ② Understanding — the idea in plain language
Picture two lemonade empires that each sell the same amount of lemonade.
- **Empire A** builds and owns every stand. To open a new stand, *it* pays for the wood, the cooler, the
  cart. To double, it must double its spending on physical stuff. Its profit keeps getting eaten by
  building the next stand.
- **Empire B** lets other people build and own the stands, hands them the recipe and the brand, and takes
  **10 cents of every dollar** they sell. To double, Empire B just signs up more owners — *they* pay for
  the carts. Almost all of B's profit is free.

Same lemonade, same sales — but **Empire B is capital-light.** It earns a *royalty* on other people's
capital, so its profit converts into free cash instead of being swallowed by the next build-out. That's
why investors will pay much more for Empire B's profits than for Empire A's.

## ③ Example — Domino's vs. Texas Roadhouse (real figures)
Two restaurant companies, opposite capital models. The numbers below are from each company's most recent
annual report (10-K, fiscal year 2025).

| | **Domino's (DPZ)** — *franchised* | **Texas Roadhouse (TXRH)** — *company-owned* |
|---|---|---|
| Revenue | $4.94 B | $5.88 B |
| Net income (profit) | **$602 M** | **~$406 M** |
| Net margin | **~12.2%** | **~6.9%** |
| Capex (spent on property/equipment) | $121 M | $388 M |
| **Capex as % of revenue** | **~2.4%** | **~6.6%** |
| Total assets | $1.72 B | $3.55 B |
| **Assets per $1 of revenue** | **~$0.35** | **~$0.60** |
| Profit per $1 of assets | **~35¢** | **~11¢** |

Read the table slowly. **Domino's earns *more* profit ($602M vs ~$406M) on *less* revenue** — because most
of its money comes from **royalties and supply-chain fees** on stores that *franchisees* build, own, and
operate. So Domino's barely spends on physical assets (just **2.4%** of revenue on capex) and runs on a
light asset base (**35¢** of assets per sales dollar). Texas Roadhouse **owns and operates** its
restaurants: every new location is *its* cash sunk into a building, kitchen, and parking lot — so it spends
**6.6%** of revenue on capex and carries nearly **double** the assets per sales dollar. Same industry —
restaurants — **opposite capital model.** That's why Domino's turns ~35¢ of profit out of every dollar of
assets while Texas Roadhouse turns ~11¢.

**Be honest about the trade-offs (this matters).** Capital-light is *not* the same as risk-free or always
better. Domino's funds itself with a lot of **debt** — it actually owes more than it owns (negative
shareholder equity, the result of borrowing to pay shareholders) — so the lightness comes with financial
risk. And owning real estate, like Texas Roadhouse does, gives you control and a hard asset that can rise
in value. The lesson isn't "franchising wins"; it's **learn to *see* the capital model**, because it
changes how much of a company's profit is actually free.

This is the practitioner version of Ackman's "royalty business," and it deepens **Unit 07 (moats)** and
**`notes/canon/canon-helmer-7-powers`**: the strongest businesses often pair a moat *with* a capital-light
model. *(Source for the idea: Forbes interview, Bill Ackman — distilled in `notes/media-practitioner-playbook` §3.)*

## ④ Application — your turn
**A. Spot the capital-light one (no computer needed).** Company P spends 3% of its revenue on capex and
holds 30¢ of assets per sales dollar. Company Q spends 9% on capex and holds 80¢ of assets per sales
dollar. Both earn a 10% net margin. Which one keeps more of its profit as free cash, and why?
*(P — it barely has to reinvest in physical assets, so more of the same 10% margin survives as free cash.)*

**B. Name the model.** A coffee company lets local owners build and run the cafés while it collects a fee
on their sales and barely buys any buildings itself. Capital-light or capital-heavy? What's the one-word
name for that fee? *(Capital-light; a **royalty**.)*

**C. Optional — pull it yourself (only if you have this project set up).** Compare capital models:
`python3 _ingest/edgar.py facts DPZ` vs `python3 _ingest/edgar.py facts TXRH`, and look at **Assets**
relative to **Revenues** (lower assets per dollar of revenue = lighter). No setup? Skip — A–B taught it.

### Check yourself
1. What does "capital-light" mean, in one line? *(A business that needs little spending on physical assets
   to grow, so it keeps more of its profit as free cash.)*
2. Why can two companies with the *same* margin still differ in quality? *(One may have to reinvest most of
   its profit in buildings/equipment to grow; the other keeps it.)*
3. Where in the numbers can you *see* a capital-light business? *(Low capex as a % of revenue, and low
   assets per dollar of revenue.)*
4. Name one reason capital-light isn't automatically "better." *(It can carry heavy debt; owning hard
   assets gives control and can appreciate.)*

### What's next
You can now read a company three ways: the scoreboard (Units 01–04), what it's *worth* (Units 05–06), and
the *quality* of the business — its moat (Unit 07) and its capital model (this unit). **Unit 08 — Reading
the Words** completes the set: what management's own language tells you that the numbers don't.
