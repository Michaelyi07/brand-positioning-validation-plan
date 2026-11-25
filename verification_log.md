# Verification Log — Real Run

## Environment

- OS: Windows 10/11 (Git Bash), 64-bit
- Python: CPython 3.13.14
- Dependencies: none (standard library only)

## Command and raw output

```text
$ python --version
Python 3.13.14

$ python verify_gates.py
PASS G1 question_count<=20_and==18 | found 18: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18']
PASS G2 tags_cover_[needs,alternatives,value_prop] | needs=6 alt=6 vp=6 total=18 (block sums == unique total)
PASS G3 preference_has_method | paired comparison, 3 unique pairs
PASS G3 preference_has_sample_n | 8-12 screened members, floor 8, tenure 6+ months
PASS G3 preference_has_decision_criteria | >=2/3 pairs AND >=60% top rank; no-consensus -> documented follow-up
PASS G3 preference_has_ballot_validity | incomplete ballots dropped
PASS G4 template_six_sections
PASS G4 template_field_schema | missing=[]
PASS G4 template_value_dictionary | 6 sections with type+allowed values columns
PASS G4 template_fictional_example_rows | 6 example blocks
PASS G4 csv_headers_ready | missing=[]
PASS G5 identity_scan_zero_hits | hits=[]
PASS G6 ascii_quotes_only | curly_hits=[]
PASS G7 every_question_has_purpose_flow_probe | purpose=18 flow=18 probe=18
PASS G8 screening_enum_consistent_across_files | template_has=True screening_has=True stale_variant=False
SUMMARY 15/15 gates passed - ALL PASS
```

Exit code: 0

## Rotation schedule balance check (real run, standard library snippet)

```text
rows found: 6
left counts: {'A': 6, 'B': 6, 'C': 6}
right counts: {'A': 6, 'B': 6, 'C': 6}
pair order per position: {'P1': [2, 2, 2], 'P2': [2, 2, 2], 'P3': [2, 2, 2]}
```

Interpretation: over the 6 archetype rows (each used by 2 respondents), every value proposition is left-placed and right-placed equally (6 archetypes -> 12 respondents), every pair appears in every presentation position equally, and every printed layout pair matches its pair's member statements (asserted inside the check).

## Gate-to-acceptance-criteria mapping

| AC | Gate(s) | Result |
|---|---|---|
| Interview outline <= 20 questions covering needs / alternatives / value proposition feedback | G1, G2, G7 | 18 questions; 6 needs + 6 alternatives + 6 value-proposition feedback; block sums == unique total; every question carries purpose/flow/probe |
| Preference test specifies method, sample size, decision criteria | G3 | paired comparison (3 unique pairs, balanced order); 8-12 screened members, floor 8; >= 2/3 pair wins AND >= 60% top rank; no-consensus/tie -> documented follow-up; incomplete ballots dropped |
| Recording template ready for immediate use | G4, G8 | six sections, full field schema (incl. theme_match/spend_evidence coding fields), value dictionary per section, 6 fictional example blocks, CSV headers complete, screening enum consistent across files |
| Fictional data only / no client name / no real identities | G5 | zero hits (banned words, emails, phone numbers, URLs) |
| Typography | G6 | ASCII quotes only |

## Fix history (independent review round)

An independent pre-submission review found: a rotation-table labeling mismatch (fixed: columns are now strictly pair-ID based and balance was re-verified mechanically above), screening-log schema conflict between files (fixed: single 7-column schema), Q16 administration-order ambiguity (fixed: binding order stated in guide §1/§4), counterfactual/hypothetical phrasing in Q06/Q09/Q11/Q12 (fixed: past-behavior wording), non-computable J2/J3 (fixed: frozen theme codes + theme_match/spend_evidence fields), and an inflated gate count in verify_gates.py (fixed: dynamic count, plus two new real gates G7/G8). All acceptance gates re-run green after fixes.
