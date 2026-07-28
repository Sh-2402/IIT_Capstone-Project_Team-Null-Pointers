# AI Workflow Appendix — Blinkit SLA Diagnostic

## Prompt log

| # | Phase | Prompt (summary) | What the AI produced | Used as-is, edited, or rejected? |
|---|---|---|---|---|
| 1 | SQL | Asked for help debugging a `STR_TO_DATE` error on empty strings | Explained the issue and gave the `NULLIF()` fix | Used as-is |
| 2 | Model | Asked whether `class_weight='balanced'` was worth trying | Code for the comparison | Used as-is, but we ran it and made the final call ourselves once we saw the real numbers |
| 3 | Dashboard | Asked why a Tableau chart's bars looked stacked/wrong | Diagnosed a shelf-configuration issue | Took two tries — first fix only partially worked |
| 4 | Memo | Asked it to sanity-check our README's cleaning-stats table against what we'd actually run | Flagged the numbers didn't match anything we'd computed yet | Used as-is — see below |

Most of the SQL schema decisions, the actual EDA takeaways, the choice of what to include in the model, and all the Tableau chart-building were done by us directly — the table above is really just the handful of moments we got stuck and asked for a second opinion.

## What the AI contributed

Mostly a debugging partner and a sounding board — explaining why an error was happening, or confirming whether a decision (like an outlier cutoff) made sense once we'd already looked at the data ourselves. It didn't write the analysis for us; we did the SQL queries, the cleaning logic, the chart-building in Tableau, and the model tuning by hand and just used AI when something broke or when we wanted a second pair of eyes on a judgment call.

## One moment it was confidently wrong

**What happened:** Early on, we asked for help drafting the README's cleaning section before we'd actually written or run any cleaning code. It handed back a full table of specific numbers — duplicate counts, outlier counts, a breach rate — written like it was real output, with zero indication it was a placeholder.

**How we caught it:** We noticed the numbers referenced a pipeline we hadn't built yet. It only came up because we were tracking our own progress and realized the table didn't match anything we'd actually run.

**What we did instead:** Wrote and ran the real cleaning script ourselves, then replaced every number in that table with our actual output. Funnily enough, some of the invented numbers turned out close to the real ones — which was its own lesson: numbers that look precise aren't the same as numbers that are verified.

## Judgment note

We leaned on AI for things we could check instantly — does this fix make the error go away, does this query run — and did everything else ourselves, especially anything that would end up as a stated number or claim in our final report. After the README moment, the rule basically became: nothing involving our actual data gets written down until we've seen it come out of our own code.
