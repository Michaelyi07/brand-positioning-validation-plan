# Brand Positioning Validation Plan (Design-Only Package)

Validation plan for repositioning a business membership space from "venue operator" to "industry resource connection platform". Design only — no interviews are executed by this package. All value propositions, examples and data are fictional; no client or company names are included.

## Contents

| File | Purpose |
|---|---|
| `interview_guide.md` | Semi-structured interview guide: consent block + 18 questions (Q01-Q18) in three tagged blocks — needs (Q-ND, Q01-Q06), alternatives (Q-AL, Q07-Q12), value proposition feedback (Q-VP, Q13-Q18). Each question carries purpose / flow / probe. |
| `preference_test_plan.md` | Paired-comparison preference test for three fictional value propositions (VP-A/VP-B/VP-C, 3 unique pairs, balanced order), sample 8-12 screened members (floor 8), ballot validity rules, decision criteria (>= 2/3 pair wins AND >= 60% top rank), documented follow-up rule, and the overall "positioning is validated" criteria (J1-J4). |
| `screening_criteria.md` | Sample screening: inclusion thresholds (S1-S6), exclusions (X1-X5), screening-log usage. |
| `results_recording_template.md` | Six-section fixed-field recording template (basic info, per-question log, quote log, preference results, screening log, decision log) with value dictionary and one fictional example row per section. |
| `recording_template.csv` | Copy-and-fill CSV version of the template (headers + fictional example rows). |
| `verify_gates.py` | Automated gate checks for the acceptance criteria (question count, tag coverage, test-plan completeness, template readiness, identity scan, typography). |
| `verification_log.md` | Real run output of `verify_gates.py` with environment details. |
| `manifest.json` | Machine-readable package manifest. |

## Running the checks

```bash
python verify_gates.py
```

Requires Python 3.11+ (no third-party dependencies). Exit code 0 = all gates pass; 1 = at least one gate failed. See `verification_log.md` for a recorded real run.

## How the acceptance criteria map to files

1. "Interview outline not exceeding 20 questions, covering needs, alternatives, and value proposition feedback" -> `interview_guide.md` (18 questions; G1/G2 gates) + `verify_gates.py` G1/G2.
2. "Preference test specifies method, sample size, and decision criteria" -> `preference_test_plan.md` (paired comparison; 8-12 screened members, floor 8; wins >= 2 of 3 pairs AND top rank >= 60%; ties -> documented follow-up) + `verify_gates.py` G3.
3. "Results recording template ready for immediate use" -> `results_recording_template.md` + `recording_template.csv` (fixed fields, value dictionary, fictional example rows) + `verify_gates.py` G4.
