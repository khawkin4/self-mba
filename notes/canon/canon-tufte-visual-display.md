# Note · Tufte — *The Visual Display of Quantitative Information*

> Canon · Cluster: Information & Communication · Maps to **Course 07** (Data & Decision-Making)

- **Source:** Edward Tufte, *The Visual Display of Quantitative Information* (1983)
- **Core claim:** Data visualization is a discipline with principles: **let the data speak, strip
  everything that doesn't.**
- **Framework:**
  - **Maximize the data-ink ratio** — every mark on the page should encode data, not decoration.
  - **Chartjunk** — gratuitous gridlines, 3-D effects, gradients — doesn't just look bad, it
    *actively interferes* with understanding. Erase it.
  - **Small multiples** — repeating the same chart structure across categories/time; one of the most
    powerful and *underused* techniques (the eye learns the frame once, then compares).
  - **The lie factor** — the ratio of the visual effect's size to the data's actual change; >1 means
    the graphic distorts (truncated axes, area-for-length).
- **Applies when:** presenting any quantitative argument — dashboards, board decks, analyses — where
  the format can either reveal or obscure the message.
- **Breaks when:** Tufte's **minimalism can go too far** — maximal data-ink isn't always maximal
  *comprehension*; some redundancy, labeling, or "junk" (a reference line, light gridlines, a touch
  of color) genuinely **aids** a non-expert audience, and modern research on *preattentive* cues and
  even "chart-junk that aids memorability" pushes back on purity. The principles also assume a
  **reader studying a static page**; interactive/dashboard/mobile contexts change the rules.
- **Practitioner counterpoint:** (fill via `research` → r/dataisbeautiful, r/datascience) — analysts
  keep **kill chartjunk** and **small multiples** as the highest-ROI habits, while noting Tufte
  purism can produce technically-correct charts non-experts can't read. Pairs with Minto for the
  *narrative* around the chart ([[canon-minto-pyramid-principle]]) and Shannon on fidelity
  ([[canon-shannon-information-theory]]).
- **Links:** [[canon-minto-pyramid-principle]] · [[canon-shannon-information-theory]] ·
  [[canon-duarte-resonate]]

---
### Rep
Take one chart you'll present. Delete every element that isn't data (gridlines, 3-D, legend clutter).
Could it become a **small-multiple** instead of one busy chart? Check the axis for a **lie factor**.
