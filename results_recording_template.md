# Results Recording Template

Ready-to-use fixed-field template for the positioning validation interviews. Every section has a fixed column schema and a value dictionary; free text is confined to designated fields. Copy `recording_template.csv` and fill one row per record per section (lines starting with `#` in the CSV are section labels — comments, not data). Zero setup required. All example rows are fictional.

## Section A — Basic info (one row per interview)

| Field | Type | Allowed values / format | Notes |
|---|---|---|---|
| record_id | string | `REC-` + 3 digits (`REC-001`…) | unique per interview |
| respondent_code | string | `R` + 2 digits (`R01`…) | links across all sections |
| role_code | enum | `founder` / `bizdev` / `marketing` / `other_ops` | from screening (S4) |
| consent_status | enum | `recorded` / `notes_only` / `declined` | `declined` stops the interview |
| consent_form_id | string | `CF-` + 3 digits, or `n/a` | consent record reference; required when consent_status is `recorded` or `notes_only` |
| date | date | `YYYY-MM-DD` | interview date |
| duration_min | integer | 30–90 | actual length in minutes; planned length is 45–60 (screening criterion S6) |
| mode | enum | `onsite` / `online` / `phone` | interview format |

Fictional example row:
```csv
record_id,respondent_code,role_code,consent_status,consent_form_id,date,duration_min,mode
REC-001,R01,founder,recorded,CF-001,2027-01-10,52,online
```

## Section B — Per-question log (one row per question answered)

| Field | Type | Allowed values / format | Notes |
|---|---|---|---|
| question_id | enum | `Q01`…`Q18` | from `interview_guide.md` |
| answer_summary | text (<= 300 chars) | interviewer's factual summary | no invented content |
| probe | text | probe questions actually used | `-` if none |
| critical_incident | enum | `yes` / `no` | `yes` = concrete episode with measurable cost or outcome |
| theme_match | enum | `TC-NET` / `TC-KNOW` / `TC-ONE` / `none` / `other` | needs-block answers (Q01–Q06) only; `-` elsewhere; codes frozen per `preference_test_plan.md` §6 |
| spend_evidence | enum | `yes` / `no` / `unclear` / `-` | alternatives-block answers (Q07–Q09) only; `yes` = concrete time or money spent stated |

Fictional example row:
```csv
question_id,answer_summary,probe,critical_incident,theme_match,spend_evidence
Q02,hardest_part=vetting_supplier_reliability;two_weeks_delayed,"why was that hard? what did you check?",yes,-,-
```

## Section C — Quote log (one row per kept verbatim quote)

| Field | Type | Allowed values / format | Notes |
|---|---|---|---|
| quote_id | string | `QT-` + 3 digits (`QT-001`…) | unique per quote |
| verbatim_anon | text | exact words, company/person names masked as `[company]` / `[name]` | never paraphrase |
| respondent_code | string | `R` + 2 digits | must exist in Section A |
| external_use | enum | `approved` / `restricted` | needs separate approval before any external use |

Fictional example row:
```csv
quote_id,verbatim_anon,respondent_code,external_use
QT-001,"finding the right partner took us [company] almost a quarter",R01,restricted
```

## Section D — Preference results (one row per pair, plus one ranking row per respondent)

| Field | Type | Allowed values / format | Notes |
|---|---|---|---|
| pair_id | enum | `P1` (A vs B) / `P2` (A vs C) / `P3` (B vs C) / `RANK` (ordinal ranking task) | rotation schedule per test plan §2 |
| winner | enum | `VP-A` / `VP-B` / `VP-C` / `tie` / `-` | pair rows only; `tie` allowed after one tie-break probe; `-` only when pair unanswered (ballot invalid, INV-2) |
| respondent_code | string | `R` + 2 digits | must exist in Section A |
| rank | string | 3-code sequence like `VP-B>VP-A>VP-C`, or `-` for pair rows | ordinal ranking from Q16; `-` for pair rows |

Fictional example rows:
```csv
pair_id,winner,respondent_code,rank
P1,VP-A,R01,-
P2,VP-A,R01,-
P3,VP-B,R01,-
RANK,-,R01,VP-A>VP-B>VP-C
```

## Section E — Screening log (one row per screened criterion, filled before invitation)

| Field | Type | Allowed values / format | Notes |
|---|---|---|---|
| screen_id | string | `SC-` + 3 digits | unique per candidate |
| respondent_code | string | `R` + 2 digits | assigned at screening, kept through the interview |
| criterion | enum | `S1_status` / `S2_activity_6mo` / `S3_tenure` / `S4_role` / `S5_industry_quota` / `S6_reachability` / `X1_competitor` / `X2_insider` / `X3_recent_research` / `X4_consent` / `X5_channel` | per `screening_criteria.md` §3 (single source of truth) |
| value | string | raw observed value (e.g., `7_interactions`, `14_months_band_6-24`) | what was actually checked |
| pass | enum | `pass` / `fail` / `excluded` | `excluded` = an X-criterion triggered |
| channel | string | recruitment channel (e.g., `member_directory`) | required for traceability (X5) |
| notes | string | optional context | `-` if none |

Fictional example rows:
```csv
screen_id,respondent_code,criterion,value,pass,channel,notes
SC-001,R01,S3_tenure,14_months_band_6-24,pass,member_directory,-
SC-001,R01,S2_activity_6mo,7_interactions,pass,member_directory,-
```

## Section F — Decision log (one row per decision criterion evaluated)

| Field | Type | Allowed values / format | Notes |
|---|---|---|---|
| criterion | enum | `J1_preference_holds` / `J2_needs_resonance` / `J3_investment_evidence` / `J4_data_quality` / `F1_floor_check` / `F2_tie_followup` | J1–J4 per test plan §6; F-criteria are process gates |
| observed | string | measured value, e.g. `VP-A:3/3_pairs;0.67_top_rank;valid_n=9` | raw numbers, no verdict wording |
| pass_fail | enum | `pass` / `fail` / `pending` | `pending` until floor is met |

Fictional example row:
```csv
criterion,observed,pass_fail
J1_preference_holds,VP-A:3/3_pairs;0.67_top_rank;valid_n=9,pass
```

## Usage rules

- One workbook per study batch; every row carries its linking code (`respondent_code` / `screen_id` / `record_id`).
- No section is free-form only: every field above has a type and allowed values; text fields are bounded and never replace structured fields.
- Verbatim quotes (Section C) are the raw material for positioning copy — transcribe unchanged, mask identities, and never edit into the answer summaries.
- Decision rows (Section F) are written only after the ballot-validity floor check (`F1_floor_check`, valid_n >= 8) has passed.
- Coding fields `theme_match` / `spend_evidence` (Section B) use the frozen theme codes from `preference_test_plan.md` §6; they make criteria J2/J3 mechanically computable.
