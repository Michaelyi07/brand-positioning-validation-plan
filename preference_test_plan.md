# Preference Testing Plan — Three Value Propositions (Paired Comparison)

Design-only document; all value propositions, member profiles and examples are fictional. Interviewing is not conducted as part of this plan.

## 1. Method: paired comparison

**Choice of method.** With exactly three value propositions, paired comparison is preferred over rating: a forced choice between two statements removes individual rating-scale bias (leniency, central tendency), keeps cognitive load low (C(3,2) = **3 unique pairs**), and yields directly comparable preference data from a small qualitative sample. Ranking is additionally collected as an ordinal measure (not numeric scoring) to provide the top-rank statistic. *(Rationale per Thurstone's paired-comparison tradition.)*

**The three fictional value propositions (VP-A / VP-B / VP-C):**

| Code | Fictional statement |
|---|---|
| VP-A | "Where your next opportunity comes from: a curated network of member companies, matched to your business goals." |
| VP-B | "Run your company on proven playbooks: a member knowledge base of SOPs and peer experience, ready to apply." |
| VP-C | "Everything your membership in one place: data, tools and services designed around your growth." |

The statements are deliberately neutral drafts. If the client disputes any label or wording, the disputed statement stays neutral, is tested as written, and — if flagged as biased by more than 2 interviewers before fielding — is excluded from the decision read and documented as a follow-up item (documented follow-up rule, Section 6).

**Scope note (VP-C).** VP-C is a comprehensiveness (bundling) statement. In paired comparison, such statements can attract lenient choices. This is accepted deliberately: the test measures whether the bundled direction actually beats the focused ones, the per-pair reason fields capture why, and Q15 counter-balances its pull. A VP-C win must therefore be read together with the Q14/Q15 reasons, and this note is carried into the decision log.

**Pairs:** `P1 = A vs B`, `P2 = A vs C`, `P3 = B vs C`.

## 2. Administration

1. Present each pair on two cards (left / right). Ask: "Which of these two statements is more relevant to your company — and briefly, why?" Record the winner and the reason. If the respondent cannot choose, probe once ("which of the two is closer to your company?"); if they still cannot choose, record `tie` for that pair and move on — a `tie` adds no win to either statement and the ballot remains valid.
2. **Balanced order (position-bias control):** the presentation order of the three pairs and the left/right placement of each statement are rotated across respondents according to the schedule below. Columns are fixed by pair ID — e.g., the `P1 layout` column always shows how the A-vs-B cards are placed for that respondent whenever P1 is presented, regardless of its position in the presentation order.

| Respondent slot | Pair presentation order | P1 layout (A vs B) | P2 layout (A vs C) | P3 layout (B vs C) |
|---|---|---|---|---|
| R01, R07 | P1, P2, P3 | A left / B right | C left / A right | B left / C right |
| R02, R08 | P2, P3, P1 | B left / A right | A left / C right | C left / B right |
| R03, R09 | P3, P1, P2 | A left / B right | C left / A right | B left / C right |
| R04, R10 | P1, P3, P2 | B left / A right | A left / C right | C left / B right |
| R05, R11 | P2, P1, P3 | A left / B right | C left / A right | B left / C right |
| R06, R12 | P3, P2, P1 | B left / A right | A left / C right | C left / B right |

Balance of this schedule (per VP across all 12 respondents): each statement appears left 12 times and right 12 times; each pair appears in each presentation position exactly 4 times.

3. After the three pairs, record the ordinal ranking task (interview guide Q16): "rank the three statements from most to least relevant to your goals for the coming year." Record as a ranked sequence in the `rank` field (for example `VP-A>VP-B>VP-C`; first = top).
4. The paired-comparison exercise and the ranking are administered as a structured exercise at the Q16 slot of the interview guide — after the comprehension checks (Q13) and before the reaction discussion (Q14–Q15). See the binding administration order note in `interview_guide.md` §1/§4.

## 3. Sample

- **sample_n = 8–12 screened target members** (floor = 8).
- Screening per `screening_criteria.md`: active member, tenure of 6+ months, cross-industry spread; exclusions apply (competitor staff, platform employees, recent research participants).
- Sample-size rationale: for a homogeneous group with a focused objective, qualitative studies typically reach near-saturated themes within roughly 8–12 interviews (Guest, Bunce & Johnson 2006, *Field Methods* 18(1):59–82 — 12 interviews yielded 88% of themes; Hennink & Kaiser 2022 report saturation at 9–17 interviews for homogeneous groups). The range 8–12 therefore covers theme saturation while keeping the paired-comparison exercise manageable.

## 4. Ballot validity

A ballot is **invalid (dropped)** if any of the following holds:

| Code | Condition | Detection |
|---|---|---|
| INV-1 | Consent for recording and/or note-taking not given | screening/consent fields in the recording template |
| INV-2 | One or more pair rows unanswered (missing `winner` on a `P1`/`P2`/`P3` row; `RANK` rows carry `-` by design and are not affected) | preference results section |
| INV-3 | Cyclic response: A>B, B>C, C>A (or any rotation of the cycle) | transitivity check across P1/P2/P3 winners |
| INV-4 | Ranking contradicts all three pair choices (top-ranked statement lost both of its pairs with no recorded reason) | cross-check `rank` vs pair winners |
| INV-5 | Screening criteria not met | screening log |

Cyclic responses (INV-3) may indicate the statements are too similar or the respondent answered at random. The interviewer first probes once ("you picked B over A, C over B, and A over C — help me understand what separates them"). If the cycle persists, the ballot is dropped and the reason is recorded in the decision log. `tie` pairs stay valid (Section 2, step 1) and simply add no win to either statement.

**Incomplete ballots are dropped** — never imputed. **The floor is re-checked before any decision is read**: after dropping invalid ballots, if fewer than 8 valid ballots remain, recruitment continues until the floor is met; no decision criterion is evaluated on a sub-floor sample.

## 5. Decision criteria (preference test)

Let `valid_n` = number of valid ballots (8 ≤ valid_n ≤ 12). For each statement, define:

- `pair_wins(X)` = number of the 3 unique pairs in which X wins outright (`tie` pairs add no win to either statement);
- `top_rank_share(X)` = valid respondents ranking X first / valid_n.

**A value proposition "holds" if and only if:**

1. it wins **>= 2 of the 3 pairs** (pair_wins(X) >= 2), **and**
2. it is ranked top by **>= 60% of valid respondents** (top_rank_share(X) >= 0.60).

**No-consensus rule:** if no statement meets both conditions, record "no consistent preference" in the decision log (criterion `F2_tie_followup`), attach the observed numbers (pair win-rates and top-rank shares for all three statements), and route to **documented follow-up**: refine the statements and re-test with a fresh sample, or resolve via a head-to-head variant — tracked to closure. The same rule covers any split outcome, including a tie between two statements' observed numbers. The plan does not authorize declaring any direction "validated" in this case.

These thresholds are decision rules for a qualitative sample, not statistical significance tests; any report states the rule, the sample size, and the raw counts.

## 6. Criteria for "the positioning is validated" (overall)

The positioning (leading with the winning value proposition) is declared **validated** only if **all** of the following pass, each stating indicator + threshold + data source + computation:

| ID | Criterion | Threshold | Source | Computation |
|---|---|---|---|---|
| J1 | A value proposition holds the preference test | wins >= 2/3 pairs AND top-rank share >= 60% | preference results (valid ballots) | per Section 5, on valid_n >= 8 |
| J2 | Needs resonance | >= 70% of valid respondents have at least one needs-block (Q01–Q06) answer coded `theme_match` = the winning VP's theme code | per-question log, `theme_match` field | count of respondents with >= 1 matching code / valid_n |
| J3 | Investment evidence | >= 30% of valid respondents have at least one alternatives-block (Q07–Q09) answer coded `spend_evidence` = `yes` | per-question log, `spend_evidence` field | count / valid_n |
| J4 | Data quality | invalid ballots <= 20% of collected ballots AND every drop has a recorded reason | screening log + decision log | drops / collected |

**Frozen coding rules (fixed before the first interview, recorded in the decision log):** each VP maps to exactly one theme code — VP-A → `TC-NET` (curated network / resource matching), VP-B → `TC-KNOW` (knowledge base / SOP playbooks), VP-C → `TC-ONE` (one-stop bundled portal). At transcription time the interviewer codes each needs-block answer with `theme_match` (enum: `TC-NET` / `TC-KNOW` / `TC-ONE` / `none` / `other`) and each alternatives-block answer (Q07–Q09) with `spend_evidence` (`yes` only when the respondent states concrete time or money spent on any current alternative; else `no` / `unclear`). With the codes frozen, J1–J4 are mechanically computable by a single evaluator and reproducible by any second evaluator from the recording template alone.

All four pass → "positioning validated", with the winning statement named and raw counts attached. Any criterion failing → "not validated", with the failed criterion IDs, observed values, and the follow-up action recorded in the decision log. Aggregate statements like "results look good" without these numbers are not acceptable outputs of this plan.

## 7. Outputs and traceability

- Per-respondent: one row set per section of `results_recording_template.md` (preference results section carries `pair_id`, `winner`, `respondent_code`, `rank`).
- Aggregate: win matrix (asymmetric 3x3), pair win-rates, top-rank shares, J1–J4 evaluation — all reproducible from the recording template alone.
- Rotation schedule, screening log, and ballot-validity reasons are retained so the sampling and decision process can be audited.
