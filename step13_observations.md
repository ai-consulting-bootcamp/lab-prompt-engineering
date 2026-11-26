## Observations: Step 13 Last Batch (15 Runs Each, v3 Prompts)

- **Sentiment (`100.0%`, `15/15`):** Completely deterministic `POSITIVE` output across all 15 runs with zero extra text or formatting drift.
- **Extraction (`64.3%`, `10/15`):** Valid JSON and exact schema on all 15 runs; minor variance came from singular vs. plural `"item"` (`"ceramic mug"` vs. `"ceramic mugs"`) and short vs. full-phrase `"issue"` (`"chipped handle"` vs. `"one arrived with a chipped handle"`).
- **Product (`50.0%`, `8/15`):** Grounded in facts and locked to `Title:` / `Summary:`, with small wording swaps (`"Enjoy"` vs. `"Experience"`, optional adjectives) and trailing spaces keeping exact-string match at `50.0%`.
- **Complaint (`0.0%` exact-string, `1/15`):** Routing was `100%` (`15/15` `Escalate: YES`), while free-form `Reply:` and `Reason:` wording made all 15 full strings unique and `escalations@example-support.test` appeared in `11/15` runs.
- **Store (`71.4%`, `11/15`):** Accurate name, synthetic address (`742 Maple Avenue, Suite 2B, Portland, OR 97205`), and hours across all 15 runs, with slight phrasing and `9 AM` vs. `9AM` spacing differences.

---

## Full Evaluation & Suite Observations (Including Recorded Personal Observations)

### Personal Observations Recorded Across This Conversation
- **Consistency Metric Definition:** Tracked repeatability using the consistency formula `((top_count - 1) / (n - 1) * 100)` across multi-run evaluations.
- **1-Shot + CoT Drop in Consistency:** Noted that combining one-shot examples with Chain-of-Thought caused exact-string consistency to drop to `0.0%` across tested runs.
- **1-Shot, No CoT & Routine-Ask Routing:** Targeted routing refinement by pairing a single example (without CoT) with explicit handling for routine inquiries.
- **Prompt Version & Shot Visibility:** Highlighted the need to clearly identify what `v3` prompts were being used and which shot/CoT configurations were applied during evaluation.

### Cross-Run & Suite-Wide Takeaways
- **Exact-String vs. Functional Reliability:** Tightly constrained outputs achieve high exact-string consistency (`100.0%` on Sentiment, `71.4%` on Store, `64.3%` on Extraction, `50.0%` on Product), whereas conversational prose (`Reply:` and `Reason:`) yields `0.0%` exact-string match even when routing decisions (`15/15` `Escalate: YES`) and factual grounding (`15/15`) hold steady.
- **Richness vs. Determinism Trade-Off:** More expressive, retail-style descriptions increase naturalness and variety but lower exact-string repeatability compared to concise, structured prompts (such as the earlier `21.4%` consistency on richer multi-attribute retail copy vs. `50.0%` in this `v3` run).
- **Routing & Policy Enforcement:** Combining 1-shot examples (without CoT) and explicit `YES`/`NO` rules for routine questions stabilizes routing decisions, though enforcing mandatory fields (like `escalations@example-support.test` on `15/15` escalations) and stripping trailing whitespace remain worthwhile polish items.
