# Note · Shannon — *A Mathematical Theory of Communication*

> Canon · Cluster: Information & Communication · Maps to **Course 07** (Data & Decision-Making), **E7** (Exec Presence & Comms)

- **Source:** Claude Shannon, *A Mathematical Theory of Communication* (1948)
- **Core claim:** **Information is the reduction of uncertainty.** A message is more informative the
  more *surprising* it is — and reliable communication over a noisy channel requires **redundancy**.
- **Framework:**
  - **Information = surprise** — a perfectly predictable message carries zero information; entropy
    measures uncertainty/surprise.
  - **Channel capacity** — there's a hard limit to how much information a channel can reliably carry.
  - **Noise** corrupts messages; **redundancy is error-correction, not waste** — repeating /
    re-encoding the signal is how it survives the channel.
  - Leadership translation: **most communication fails because the channel is noisy** (distraction,
    competing messages, misunderstanding). The fix is **intentional redundancy** — say the important
    thing multiple ways through multiple channels. *If you said it once, you haven't said it.*
- **Applies when:** any communication that *must* land — a strategy, a change message, a safety-
  critical instruction — across a noisy organization.
- **Breaks when:** **redundancy has a ceiling** — past a point, repetition becomes noise itself
  (everything "urgent" = nothing urgent), and over-communication breeds tune-out. The math is about
  *fidelity of transmission*, **not meaning, persuasion, or whether the idea is any good** — a
  perfectly transmitted bad message is still bad (that's Minto/Sinek/Duarte's domain,
  [[canon-minto-pyramid-principle]]). Don't over-literalize a 1948 engineering theorem into a theory
  of leadership.
- **Practitioner counterpoint:** *(researched 2026-06-05 — Discern/Computerphile/Art-of-the-Problem transcripts; reddit corpus thin)*
  The teachers who explain Shannon all converge on the same warning the leadership translation
  glosses over: **the 1948 math is deliberately about transmission, not meaning.** Shannon himself,
  in his own recorded words, says *"to measure information you have to look at it without regard to
  meaning… content is irrelevant"* (Discern). Practitioners (computer-science explainers) push the
  same line in the other direction — the maxim leaders relearn that **"you have to say it multiple
  times before it lands"** is just Shannon's redundancy/error-correction in the wild, but the math
  only guarantees the *bits* arrive, not that the *idea* was good. Bungay's *alignment gap* is the
  same redundancy idea in command language ([[canon-bungay-art-of-action]]).
- **Researched layer** *(2026-06-05)*
  - **Canonical explanation (sourced):** Shannon's core move is to strip meaning out so information
    can be *measured* like energy. In his own recorded words: *"I wanted to try to find a way to
    treat information like a physical thing… to measure information you have to look at it without
    regard to meaning… the point of sending a message is to remove uncertainty"* (Discern, "Claude
    Shannon Explains Information Theory"). The unit is the **bit** — one fair coin toss — and
    *"if something's completely predictable there's zero information; if something's completely
    random you need information about everything."*
  - **The mechanism, verified across transcripts:** information = **surprisal**, formalized as
    *I(e) = log(1/p)* — *"every time you halve the probability you only increase the amount you're
    surprised by by literally a bit"* (Computerphile, "Why Information Theory is Important").
    **Entropy** is the *average* surprise: the Art of the Problem video reframes it as **the minimum
    number of yes/no questions you'd expect to ask** — a uniform 4-symbol source needs 2 questions
    per symbol, but a skewed source needs only **1.75**, so it *"is producing less information
    because there is less uncertainty or surprise about its output."*
  - **Real application (mined):** the corpus grounds the theory in working engineering, not metaphor —
    *"things like compression, zip files, network error-correction codes… are all directly related
    to information theory"* (Computerphile). The hard-limit payoff: *"if you know the throughput in
    bits of a channel… there's no smart way of putting more information through it than whatever that
    number is"* — channel capacity as a literal ceiling, and entropy as the floor below which you
    *"can never do better than this on average"* when compressing.
  - **Where the corpus pushes back on the book:** the explainers are emphatic that Shannon's quantity
    is **content-free** — *"that upset a lot of people, that content is irrelevant"* (Discern). The
    math certifies that the *bits* survive the noisy channel; it says nothing about whether the
    message persuades or whether the idea is worth transmitting. That's exactly the note's
    "breaks-when": don't over-literalize a 1948 transmission theorem into a theory of meaning or
    leadership ([[canon-minto-pyramid-principle]]).
  - **Sources in corpus:** Discern — "Claude Shannon Explains Information Theory"
    (youtube.com/watch?v=1afrzErFy_k) · Computerphile — "Why Information Theory is Important"
    (youtube.com/watch?v=b6VdGHSV6qg) · Art of the Problem — "Shannon's Information Entropy (Physical
    Analogy)" (youtube.com/watch?v=R4OlXb9aTvQ). *(reddit r/dataisbeautiful pull present in corpus
    but off-topic — generic top-posts listing, no Shannon/info-theory practitioner thread; flagged
    for targeted re-pull of r/compsci / r/ExperiencedDevs.)*
- **Links:** [[canon-bungay-art-of-action]] · [[canon-tufte-visual-display]] ·
  [[canon-minto-pyramid-principle]] · [[canon-marquet-turn-the-ship-around]]

---
### Rep
Take your most important current message. Are you relying on a single channel (one email)? Re-send
the *same core idea* through two more channels, worded differently. Assume it hasn't landed yet.
