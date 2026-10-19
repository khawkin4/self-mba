# Trading floor mechanics — how the institutions on the other side of the trade are actually organized

> **Sources — two filmed institutions:** *Inside UBS' $3b-a-day Sydney trading floor* (Markets with
> Madison, ~27k chars), a tour of a 117-person bank floor with the executive who runs it; *Inside One
> of the World's Top Proprietary Trading Desks* (SMB Capital, ~16k chars), a 50-trader prop firm
> filmed across one intern's day. **Plus six role-structure sources** (~49k chars): a former J.P.
> Morgan analyst comparing IB / equity research / S&T; a buy-side equity research analyst in
> conversation; a Morgan Stanley S&T VP's hour-by-hour day; front/middle/back office; buy-side vs
> sell-side; S&T explained. Raw at `_ingest/raw/2026-09-26/media/{workflows,institutional}/`.
>
> **Why this note exists:** the program can read any company's filings and price any security, and has
> no picture of the **institution on the other side of the trade** — how a floor is divided, who
> actually decides, how information is walled off, and how professional judgment is drilled. That is
> tacit, organizational knowledge; it is not in EDGAR and not in the canon. It is also the layer that
> [[bloomberg-terminal-instrumentation]] kept gesturing at without describing: the `IB` network and
> the $30k seat only make sense once you can see the floor they sit on. Maps to **Course 06**
> (Operations), **Course 09** (Leadership & Org Behavior), **Course 11** (Global Strategy & Macro),
> **E8** (Stakeholder & Investor Relations), and — most usefully — to `acumen/MECHANISM.md`.
>
> **Provenance:** §§1–5 and §7 are from the sources. §6 is this note's own comparison; §8 is the
> program-integration argument and the triangulation in §3c is this note's, not any source's.
>
> ⚠ **Every institution here is self-presented.** The SMB film is a recruitment video ending in a hard
> sales pitch; its headline statistics are marketing and are flagged as such in §5. The UBS film is a
> sanctioned PR tour on a literally prescribed route. The role-structure sources are career-content
> creators, several selling something. Read all of it as *shape*, not as audit — hours, pay bands and
> headcounts especially.

---

## 1 · Two institutions, two shapes

| | **UBS Sydney** | **SMB Capital** |
|---|---|---|
| Type | Bank markets division | Proprietary trading firm |
| Headcount | 117 on the floor | 50+ traders |
| Whose money | Clients', plus principal risk | The firm's |
| Turnover | A$8–10bn securities/day, ~20% of ASX | Not disclosed |
| Organizing unit | Three businesses, 22 risk buckets | Desks + intern teams |
| What it optimizes | Risk-adjusted return **and** client service | Trader development |
| Traders as share of staff | **15–20%** | Nearly all |

The last row is the one that reframes everything. On a bank "trading floor," four in five people are
not traders. The rest are research, sales-trading, advisory sales, and support — roughly **40
distinct jobs**. The program's mental image of finance is almost entirely the 15%.

---

## 2 · The two axes that organize the entire industry

Everything in finance sits somewhere on two independent axes. Learn these and most job titles decode
themselves.

### Axis 1 — buy side vs. sell side

| | **Sell side** | **Buy side** |
|---|---|---|
| Does what | Raises capital for companies, sells securities, advises on deals | Invests other people's money |
| Earns from | Fees and commissions — *volume* | Management fee (regardless of outcome) **+ performance fee, typically ~20% of gains** |
| Incentive it creates | Sell more, to more clients | Be right, and be right in a way you can hold |
| Who | Investment banks, brokers | Asset managers, hedge funds, PE, VC, pension funds |
| Entry-level roles | **Plentiful** — IB, ER, S&T all recruit undergrads | Scarce; typically wants 2–4 years first |

The two depend on each other completely: the sell side prices and distributes what the buy side buys.
And the naming is genuinely confusing — **the big banks run both.** J.P. Morgan, Goldman and UBS all
have asset management arms that are buy side. When someone says "sell side," they mean the investment
banking division specifically.

The compensation difference at entry is small (both roughly six figures including bonus); the *skill*
divergence is large and arrives with seniority. **Senior sell side becomes a salesperson. Senior buy
side becomes a researcher and modeller.** That is the fork worth knowing before choosing a first job.

### Axis 2 — front / middle / back office

Orthogonal to the first, and it is purely about client contact:

| | Who | Job |
|---|---|---|
| **Front** | IB, S&T, research | Face the client. Generate revenue |
| **Middle** | Risk management, compliance, finance control, strategy | **Check the front office** — ensure it isn't out of compliance or taking risk the bank shouldn't hold |
| **Back** | Technology, operations | Make it run. No client contact |

The middle office exists to constrain the front office, which means the bank is deliberately built
with an internal adversary. Worth holding next to §4's carpet and meeting separation: **a bank's
org chart is substantially a risk-control artifact**, not a productivity one.

---

## 3 · Three sell-side seats, compared

The clearest single source here is a former J.P. Morgan analyst comparing the three front-office
tracks. Condensed:

| | **Investment Banking** | **Equity Research** | **Sales & Trading** |
|---|---|---|---|
| Core output | M&A and capital raising | Reports that inform investors | Execution and market making |
| Junior does | Excel models, PowerPoint pitchbooks, filing/industry research, meetings | The research, the operating models, the write-ups | Learns the book, the flow, the clients |
| Senior does | Originates deals | Relationships with management teams and investors | Relationships and risk |
| Hours | **70–100/wk** as analyst; 60–90 associate; 50–80 VP; 40–60 director | 60–70 average, **spiking past 100 at earnings** | Market hours — early start, hard stop |
| Weekends | 0–20 hrs, only on live deals | **Saturdays are sacred** | Largely free |
| Team shape | One analyst + one associate per deal | 3–6 people covering 10–30 companies | Flat — analysts sit beside MDs |
| Tools | *"PowerPoint and Excel"* | *"Word docs and Excel"* | ***"Bloomberg and your phone"*** |
| Exit options | **Widest** — PE, hedge funds, corp dev, IR, operations | Same minus PE; many to hedge funds | **Narrowest** — markets only |

Three structural facts that matter more than the table:

**1. The banking hours are driven by secrecy, not volume.** M&A is confidential to a handful of
C-suite executives, so deals are compressed to limit leakage — and each deal team is *one analyst and
one associate.* The 100-hour week is a consequence of a small team holding a fast, secret process. And
it is bursty: with no live deal, analysts leave at 8–10pm with no weekend work.

**2. Two of the three seats are structurally shrinking.** Equity research is contracting *"due to
data being so widespread and accessible via the internet"* — the exact thesis this program is built
on, eroding an industry from underneath. And S&T is contracting through automation, with one figure
that should be read twice: **Goldman's cash equities desk went from ~600 traders in 2000 to 2.**

**3. Hierarchy is near-identical in IB and S&T** — analyst → associate → VP → director → MD, roughly
2–3 years to VP and 3–5 more to MD — but equity research is idiosyncratic: you *start* as an associate,
get promoted *to* analyst, and every level above (VP, SVP, director, MD) is still called an analyst.

### The day, hour by hour

A Morgan Stanley S&T VP's actual schedule, which is the most concrete artifact in the corpus:

| | |
|---|---|
| 04:00 | Up |
| 06:00 | At the desk. Breakfast there |
| 07:00 | **Global S&T call** — clients, markets, urgent updates |
| 08:00 | **Team meeting**, ~30 min |
| 08:30–09:30 | Overnight email from a global team. *"Even if you don't have answers, let people know you've read them"* |
| 09:30–12:00 | Yesterday's unfinished work |
| 12:00 | **Lunch at the desk** — protocol, because everyone woke at 4 |
| 12:30–14:00 | New projects |
| 14:00 | Coffee run, ~15 min |
| 14:30–close | **Meetings and 1:1s** — the only window, because colleagues are with clients until then |
| 17:45–18:00 | Out |

Sleep: four and a half to five hours, *"my entire tenure there from associate through VP."* Note the
shape rather than the heroics — **the only uninterrupted work block is 09:30 to 12:00**, and meetings
are pushed to the back of the day because client duty owns the front of it.

---

### 3c · Buy-side vs. sell-side research — and the principle underneath

The two do the same nominal job and are not the same activity at all. From a buy-side analyst
describing the difference directly:

| | **Sell-side report** | **Buy-side report** |
|---|---|---|
| Shape | *"Here's what happened, here's kind of what we think, here's a target price"* | *"What are the actual drivers… why does this company exist, who are they taking money from, how would you estimate the actual market"* |
| Length | Initiation 20–100pp; updates 1–10pp | Initiation **40–50pp**, and denser |
| Published? | Yes — that's the product | **No.** Proprietary, written for the PM |
| Being wrong costs | *"Maybe affects your ranking on Bloomberg, but that's about it"* | *"How much money can you lose, and how much would that lose for clients"* |

Note the asymmetry in the last row. It is the entire explanation for why buy-side work is more
qualitative and more paranoid: **the consequence of error is denominated differently.**

And then the practice that should be lifted into this program wholesale. Buy-side analysts *do* take
the sell-side model — but only the reported financials, because *"it's hard to mess that up"* — and
then **rebuild the drivers tab themselves**, refusing the assumptions entirely:

> *"You want to have your own unbiased opinion… otherwise you don't have an opinion. If you're always
> consensus, just take their target price — you don't have to model it."*

You may look at the other analyst's conclusion **afterwards**, as a challenge to your own: *"why are
you guys higher by this much, how'd you get to this valuation, I'm getting something different."*
Order matters. Consensus consulted after you have a view is a stress test; consulted before, it is an
anchor. Straight [[canon-kahneman-thinking-fast-and-slow]].

> **The triangulation.** Three independent sources, three different seats, one principle:
>
> - [[sec-filing-intelligence]] — Layer 1 (facts) is a commodity; Layer 3 (judgment) is the product.
> - **Damodaran**, from a live Terminal — take the raw data; refuse Bloomberg's computed cost of capital because it is opaque; *"it's my job to estimate"* those ([[bloomberg-terminal-instrumentation]] §1).
> - **A working buy-side analyst** — take the reported financials; rebuild the drivers; hold consensus at arm's length until you have your own number.
>
> **Accept the facts. Refuse the judgment. Build your own.** That is one sentence, arrived at
> independently by a data architecture, an academic, and a practitioner — and it is, exactly, what
> this program is for. It is also the sharpest available argument that `learn/`'s insistence on
> hand-computation (`learn/README.md` rule 2) is not pedagogical fussiness but professional practice.

One scale marker to keep the romance out of it: a PM in this analyst's firm tracks **50–100 companies**
and works most weekends, covering an international fund across Asian market hours as well.

---

## 4 · The bank floor as an organizational machine

### The split that defines everything: risk vs. client

> *"Responsibility sits with the trader to take all of the risk, and then the client servicing group
> works around that trading business… The salesperson in each division is client-facing, the other's
> managing the risk. They're different roles."*

The floor's own analogy: the salesperson is who you meet at the car yard; the trader is the person
who owns the lot and is actually buying and selling the car. **Pricing and risk sit with one person;
the relationship sits with another.** Every other structure on the floor — meetings, seating,
information barriers — follows from keeping those two things apart.

### Information barriers are physical and temporal, not just policy

The single most instructive detail in either source. UBS's Chinese walls are implemented in **carpet
colour**:

- **Dark grey carpet** — no phones, no cameras. Sensitive market information is on the screens.
- **Light grey carpet** — visitors may walk and talk.

And in **the meeting calendar**:

| Time | Meeting | Why it is separate |
|---|---|---|
| 5:30–5:45am | Equities team arrives | — |
| 7:30 | **Flow** meeting | Client flow |
| 7:45 | **Research analyst** meeting | *"Those groups need to be segregated. We keep client flow away from different parts of the business."* |
| 8:00 | **Rates** meeting | Macro, after the bottom-up |

Two meetings fifteen minutes apart that could trivially be one, held separately *because* combining
them would leak client flow into research. The compliance requirement has been converted into
architecture and calendar rather than a policy nobody reads. That is a systems-design lesson worth
more than the finance content: [[canon-meadows-thinking-in-systems]] — when you want a rule obeyed,
build it into the structure so that breaking it requires deliberate effort, rather than relying on
the agent's intention.

Note also the sequence: **bottom-up before macro.** Equities flow and research at 7:30/7:45, rates
and macro at 8:00.

### Sound as an instrument

> *"Those different sounds reflect a different trade… by hearing that sound you don't need to look at
> what's happened, you know what's happened."* … *"When it gets really loud, you hear that sound
> you're used to hearing over and above every other sound."*

The floor is audibly encoded — a futures contract trading sounds different from an equities print,
and traders are tuned to their own. This is a redundant sensory channel deliberately maintained for
exactly the conditions where the visual channel saturates. The stated reason:

> *"When it's crazy, that's when mistakes happen… it's a bit like a sporting team. You can train all
> you like, but in a grand final in the last five minutes, that's when the game's won or lost. So we
> try and hardcode individuals to operate under stress."*

### How large orders actually move — the part the program can't see from filings

This is the concrete mechanics behind [[market-structure-24-5-trading]]'s liquidity arguments:

- **Block threshold:** ~$10m, *or* more than one day's average trading volume.
- **Frequency:** the market sees 5–10 smaller blocks a day; the large ones come weekly, monthly, or quarterly.
- **Timeline:** a $262m block took two to three days to source and negotiate. The largest NZ block cited — Auckland Council's $1.3bn Auckland Airport sell-down — was a negotiated transaction, not a market order.
- **Wall crossing:** sourcing a block privately means handing a counterparty material non-public information under restriction. Named explicitly as routine.
- **Six execution platforms** for a single equity order. The choice is a four-way trade-off: *commission, speed, size, discretion.*
- **The facilitation desk** takes principal risk — the bank buys your line onto its own book. *"Probably not the cheapest way to get it done, but it gets what you want done."*

And a candid statement of why scale is itself discretion: *"It's hard to see a high-volume trade when
UBS is involved, when you're 20% market share."* Market share functions as camouflage. That is a
[[canon-helmer-7-powers]] scale economy operating as a *client-facing feature*, not a cost advantage.

### Verification discipline

> *"Your first reaction isn't the right reaction. It's an emotional reaction based on something you've
> seen. Is what you've seen accurate and verified?… Generally we'll need things verified before
> acting. Particularly if a client's orders are involved. We're not about to risk that on the sake of
> an X headline."*

News no longer arrives only through the Terminal. The institutional response is not faster
consumption but an interposed verification step — a deliberate latency *added* on the client-order
path. Worth sitting next to [[bloomberg-terminal-instrumentation]] §3: institutions pay enormous sums
to reduce latency and then voluntarily reinstate some of it where being wrong is unrecoverable.

### On AI, from someone deploying it

117 Copilot licences across the team. The honest part:

> *"I think we're still grappling with how we monetize it… It makes what we do more efficient and
> quicker, which is great for clients. I can't see people paying for that improved efficiency. It's
> just expected. We're in the service industry."*

Efficiency gains in a service business are competed away into client expectation rather than captured
as margin. Direct counterpoint to [[professional-services-leverage]] §6 — and the same structural
question, asked by someone paying for the licences.

---

## 5 · The prop desk as a learning machine — and the mechanism finding

SMB's daily loop, as filmed:

1. **AM meeting** — the setups to be traded that day are named and their conditions specified. (*"You need to understand the setup where this is going to work exceptionally well, because otherwise you're subjecting yourself to all sorts of things that you can't control."*)
2. **The open** — traded live, with the whole desk on a voice channel and a text channel simultaneously. Ideas and reads are shared intraday.
3. **11am meeting** — teams present. The explicit instruction: *"As we go through the teams, please talk about a trade that did not work."*
4. **Daily report card**, reviewed every day, with a coach.

> **This is a working instance of the exact three-leg mechanism `acumen/MECHANISM.md` specifies — and
> it turns every single day.**

| Leg | `acumen/MECHANISM.md` | SMB, observed |
|---|---|---|
| **Tool** | Six-dimension rubric, memo spec | The playbook: setups with defined core metrics, graded **A+ / A / B / C** |
| **Adoption** | One scored rep/week, skipped weeks logged | AM meeting → live trade → 11am presentation. Daily, mandatory, and **competitive** (teams contest a sword) |
| **Inspection** | Rubric score, monthly ledger read | Daily report card with a coach who presses on the decision narrative |

Three design features worth stealing:

**1. The agenda item is failure.** The meeting does not ask "what did you do." It asks for *a trade
that did not work.* Disconfirming evidence is not something the reviewer must extract — it is the
price of admission to the room. `MECHANISM.md` scores what you did; this **selects for what didn't**,
which is a structurally different and stronger inspection leg.

**2. The review target is the narrative, not the outcome.** The coach:

> *"Map out what was that mental story you were telling yourself during that execution, and key in on
> what was that key thing that made you hold for longer than you should have."*

The intern's own account of the mechanism working: he held a failed breakout through three separate
exit signals, lost half a daily stop, and the lesson extracted was *"when I see these strong signs to
exit, I should just exit — if a better setup presents itself I can always re-enter."* The reviewable
unit is the decision process at the moment of the decision, recoverable only because it was written
down the same day.

**3. The stated objective is calibration, in plain language.**

> *"The gap between what's actually happening and our perception of what's happening is pretty large
> almost all the time. Especially for developing traders, your goal is to narrow that gap."*

That is `MECHANISM.md`'s **calibration error** input, stated as the entire purpose of the training
program rather than as one metric among five. Also straight [[canon-kahneman-thinking-fast-and-slow]].

Two further transferable details: interns build playbooks as **graded taxonomies** (define the setup,
define the metrics that distinguish an A+ from a C, then defend classifications with examples) — which
is a rubric-construction exercise, not a content exercise. And risk is discussed in **units of daily
stop** (*"I was up like two daily stops on this, but ended up only getting out for half a daily
stop"*), which normalizes P&L into a bounded, comparable scale before it is ever discussed.

⚠ **Marketing, not evidence.** The video closes by claiming a UC Davis study of "tens of millions of
trades spanning 15 years" showing 99% of active retail traders never reach consistent profitability,
and that SMB's traders succeed at "20 to 40 times the rate" of retail. Both appear inside a sales
pitch for a paid product; neither is sourced on screen. The underlying academic literature
(Barber & Odean and the Brazilian day-trading studies) supports *directionally* poor retail outcomes
but not these specific figures, and a firm's self-reported success multiple against an unmatched
comparison group is not a measurement. **Do not cite these numbers.** The mechanism above stands on
its own without them.

---

## 6 · What crosses over, and what does not

| | Bank floor | Prop desk |
|---|---|---|
| Primary constraint | Regulation, client duty, reputation | Firm capital |
| Failure mode feared | A compliance breach or a client's order mishandled | A trader who never becomes profitable |
| Barriers | Enforced *between* groups (carpet, meetings) | Deliberately *removed* (voice channel all day) |
| Review | Risk systems, oversight, "microscopically overseen" | Daily coached review of the decision narrative |
| Information sharing | Restricted by design | Maximized by design |

The two are near-inversions on information flow, and for a coherent reason: the bank's risk is that
information moves *between the wrong groups*; the prop desk's risk is that it fails to move *between
the right people fast enough*. **Neither is a best practice. Each is a response to a different
liability.** Copying the open voice channel into an organization with client duties would be a
compliance incident; copying the carpet into a 50-person prop desk would destroy its only edge.

The transferable layer is narrower than it looks, and it is the SMB review loop (§3) — because that
addresses individual judgment formation, which is what `acumen/` exists to do.

---

## 7 · Where the Terminal actually sits on a floor

Both films quietly answer a question [[bloomberg-terminal-instrumentation]] could only assert.

The Terminal is **not the floor's nervous system.** At UBS the primary real-time channels are
proprietary risk systems, the squawk, the ambient sound of the room, and the phone; news increasingly
arrives via X and is *deliberately slowed down* for verification. At SMB the traders execute through
**internal execution software**, not a vendor terminal, and coordinate on a voice channel. Neither
source mentions a Bloomberg function by name during live trading.

This sharpens rather than contradicts the earlier note. The Terminal's institutional role is
**research, reference, analytics, and — above all — `IB`, the inter-firm messaging layer.** That
matches §2 of the instrumentation note exactly: the moat is the network, not the data. What these
films add is that during the minutes that actually matter, a professional's attention is on systems
the $30k seat does not provide and a retail user could never buy.

---

## 8 · What this gives the program

**1. A rubric upgrade for `acumen/`.** Add the SMB inspection design to `MECHANISM.md`: the rep's
presentation slot should require *a call that did not work*, and the review should target the
decision narrative at the moment of decision — not the outcome. Pair with the existing constraint
audit from [[bloomberg-terminal-instrumentation]] §7. Both are cheap, and both attack the failure
mode the mechanism file already diagnosed.

**2. A missing unit's worth of vocabulary.** `learn/` teaches a beginner to read a company. Nothing in
the program teaches who is on the other side of the trade. Block thresholds, wall crossing, principal
vs. agency execution, facilitation, the sales/trader split, the sell-side research relationship — these
are the terms that make [[market-structure-24-5-trading]] legible, and several are now in `GLOSSARY.md`.

**3. An honest picture for Course 09 and E8.** The floor is a management system: 22 risk buckets, 40
job types, a "head coach" whose stated job is hardcoding people to perform under stress, and an
explicit trade-off between information barriers and information flow. That is org design with a
scoreboard attached — rarer and more useful than another leadership framework.

**4. A correction to the program's mental model.** Traders are 15–20% of a trading floor. If the
curriculum's image of institutional finance is a person with six monitors, it is picturing a minority
of a minority, and mis-pricing which careers and which skills the field actually consumes.

**5. The strongest available validation of the program's method — and it is §3c.** *Accept the facts,
refuse the judgment, build your own* is now attested by a data architecture, by the academic the
curriculum already cites, and by a working buy-side analyst, none of whom were talking to each other.
That single sentence is a better statement of what this program does than anything currently in
`README.md`, and it belongs in the argument spines rather than buried in a practitioner note.

**6. A live warning about the destination.** Two of the three front-office seats are shrinking, and
for the reason this program depends on: equity research is contracting *because* data became
"widespread and accessible via the internet," and Goldman's cash equities desk went from ~600 traders
to 2. The free-data thesis is not only a student's convenience — it is dissolving the jobs that used
to be the payoff for learning this. Worth stating plainly wherever the curriculum implies a career.

---

## 9 · Links

**Repo:** [[bloomberg-terminal-instrumentation]] (§5 here places the Terminal on a real floor; §6
extends that note's constraint audit) · [[market-structure-24-5-trading]] (block trades, dark pools,
VWAP and the closing auction, now with the desk-level mechanics underneath) ·
[[market-structure-24-5-institutional-response]] · [[professional-services-leverage]] (§2's AI
efficiency argument is the same question from the buyer's side) · [[sec-filing-intelligence]] (what
filings *cannot* show you: this) · `acumen/MECHANISM.md` (§3 and §6 — the main contribution)

**Canon:** [[canon-meadows-thinking-in-systems]] (barriers built into structure rather than policy) ·
[[canon-kahneman-thinking-fast-and-slow]] (the perception/reality gap, stated as a training objective) ·
[[canon-helmer-7-powers]] (market share as discretion — a scale economy sold as a client feature) ·
[[canon-grove-high-output-management]] (the floor as a production system; the "head coach" framing) ·
[[canon-klein-sources-of-power]] (the audible channel — recognition-primed decision under saturation) ·
[[canon-mauboussin-success-equation]] (why a firm's self-reported success multiple is not a measurement)
