# Sample Screening Criteria

Design-only document. All examples are fictional; no real persons or companies are involved.

## 1. Who qualifies (inclusion criteria)

A target member qualifies for the positioning validation sample (8–12 members, floor 8) only if **all** of the following hold. Screening happens **before invitation**, and every criterion is logged per candidate in the screening log (see `results_recording_template.md`, Section E).

| # | Dimension | Threshold | Rationale |
|---|---|---|---|
| S1 | Membership status | Active member of the business membership space in good standing | Only members can speak to membership value; inactive members produce noise |
| S2 | Activity level | >= 4 member interactions (events attended, portal logins, service requests) in the past 6 months | Distinguishes real users from nominal members; low-activity members cannot evaluate the resource-connection direction |
| S3 | Tenure | 6+ months of membership | Shorter tenure lacks the history needed for needs/alternatives questions (Q01–Q12) |
| S4 | Role | Founder/owner, or the person accountable for business development / partnerships / marketing | Positioning is being tested against growth-relevant needs; strategyzer practice prioritizes decision-relevant roles |
| S5 | Cross-industry spread | No more than 2 respondents from the same industry within the sample of 8–12 | Prevents one industry's needs from dominating the decision read |
| S6 | Reachability | Available for a 45–60 minute interview (planned length; actual duration is recorded in the 30–90 range of the template) | Operational feasibility |

Note on tenure (S3): members with very long tenure (e.g., 3+ years) are still eligible, but the sample should include both mid-tenure (6–24 months) and long-tenure (24+ months) members so that perception shifts are represented; record the tenure band in the screening log `value` column.

## 2. Exclusions (automatic disqualification)

| # | Exclusion | Reason |
|---|---|---|
| X1 | Employees, owners or affiliates of competing membership or networking organizations | Bias risk; cannot speak neutrally |
| X2 | Platform employees, contractors, or their immediate business partners | Insiders cannot represent member perception |
| X3 | Participation in any platform research study within the last 6 months | Avoids panel fatigue and repeated-sample bias |
| X4 | Did not give consent for recording and/or note-taking when asked | Ethical requirement; also renders the ballot invalid (INV-1) |
| X5 | Candidate recruited outside the agreed recruitment channels without a logged channel | Breaks traceability of the sampling process |

## 3. Screening log usage

- Criterion codes used in the screening log `criterion` field (single source of truth, mirrored in `results_recording_template.md` Section E): `S1_status`, `S2_activity_6mo`, `S3_tenure`, `S4_role`, `S5_industry_quota`, `S6_reachability`, `X1_competitor`, `X2_insider`, `X3_recent_research`, `X4_consent`, `X5_channel`.
- One row per screened criterion per candidate, filled **before** the invitation is sent.
- Schema (identical to template Section E): `screen_id, respondent_code, criterion, value, pass, channel, notes`.
  - `screen_id` = `SC-` + 3 digits (e.g., `SC-003`), unique per candidate.
  - `respondent_code` = `R` + 2 digits, assigned at screening time and kept through the interview.
  - `value` = raw observed value for that criterion (e.g., interaction count, tenure band, industry).
  - `pass` = `pass` / `fail` / `excluded` (`excluded` = an X-criterion triggered).
  - `channel` = recruitment channel; `notes` = optional context.
- A candidate is invited only when all S-criteria are `pass` and no X-criterion applies; the invited set becomes the interview roster, and the final sample is the subset completing consent and interview.
- If the valid-ballot floor (8) is not reached after drops, re-open screening and recruit additional candidates; the floor is re-checked before any decision is read (see `preference_test_plan.md`, Section 4).

## 4. Fictional example (screening log rows)

```csv
screen_id,respondent_code,criterion,value,pass,channel,notes
SC-001,R01,S2_activity_6mo,7_interactions,pass,member_directory,
SC-001,R01,S3_tenure,14_months_band_6-24,pass,member_directory,
SC-002,R02,X3_recent_research,participated_2mo_ago,excluded,member_directory,deferred_to_next_cycle
```
