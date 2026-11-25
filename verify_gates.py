"""Automated gate checks for the brand positioning validation deliverable package.

Gates:
  G1  interview guide has exactly 18 questions (<= 20 allowed by AC)
  G2  question tags cover [needs, alternatives, value_prop] with 6/6/6 blocks
  G3  preference test plan specifies method + sample_n + decision criteria
  G4  recording template: all six sections present with full field schema,
      value dictionary and fictional example rows (md + csv)
  G5  identity/bias scan: no emails, phone numbers, URLs, banned words,
      no client/real-name tokens
  G6  typography: ASCII quotes only in package text files
  G7  every question carries purpose / flow / probe
  G8  cross-file consistency: screening criterion enum identical in
      screening_criteria.md and results_recording_template.md

Exit code 0 = all gates PASS; 1 = at least one FAIL.
"""
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent
TEXT_SUFFIXES = {".md", ".csv", ".py", ".json"}

FAILS = []
CHECKS = 0


def check(gate: str, label: str, ok: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"{'PASS' if ok else 'FAIL'} {gate} {label}" + (f" | {detail}" if detail else ""))
    if not ok:
        FAILS.append(f"{gate}:{label}")


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8-sig")


def main() -> int:
    guide = read(ROOT / "interview_guide.md")
    plan = read(ROOT / "preference_test_plan.md")
    screening = read(ROOT / "screening_criteria.md")
    template = read(ROOT / "results_recording_template.md")
    csv_text = read(ROOT / "recording_template.csv")

    # G1: question inventory
    q_ids = re.findall(r"\*\*Q(\d{2})\.\*\*", guide)
    q_n = len(q_ids)
    check("G1", "question_count<=20_and==18", q_n <= 20 and q_n == 18, f"found {q_n}: {q_ids}")

    # G2: primary tag coverage per question
    tag_blocks = re.findall(r"Primary tag:\s*([a-z ]+?)\.", guide)
    tags = [t.strip() for t in tag_blocks]
    n_needs = sum(1 for t in tags if t == "needs")
    n_alt = sum(1 for t in tags if t == "alternatives")
    n_vp = sum(1 for t in tags if t.startswith("value proposition feedback"))
    covers = n_needs == 6 and n_alt == 6 and n_vp == 6 and len(tags) == 18
    check("G2", "tags_cover_[needs,alternatives,value_prop]",
          covers, f"needs={n_needs} alt={n_alt} vp={n_vp} total={len(tags)} (block sums == unique total)")

    # G3: preference test method + sample + decision criteria
    has_method = "paired comparison" in plan.lower() and "P1 = A vs B" in plan and "P3 = B vs C" in plan
    has_sample = bool(re.search(r"8[-\u2013]12", plan)) and "floor" in plan.lower() and "6+ months" in plan
    has_decision = (">= 2 of the 3 pairs" in plan) and (">= 60%" in plan) and "documented follow-up" in plan
    has_validity = "invalid" in plan.lower() and "dropped" in plan.lower()
    check("G3", "preference_has_method", has_method, "paired comparison, 3 unique pairs")
    check("G3", "preference_has_sample_n", has_sample, "8-12 screened members, floor 8, tenure 6+ months")
    check("G3", "preference_has_decision_criteria", has_decision, ">=2/3 pairs AND >=60% top rank; no-consensus -> documented follow-up")
    check("G3", "preference_has_ballot_validity", has_validity, "incomplete ballots dropped")

    # G4: recording template sections + fields + value dictionary + examples
    required_sections = ["Section A", "Section B", "Section C", "Section D", "Section E", "Section F"]
    check("G4", "template_six_sections", all(s in template for s in required_sections))
    required_fields = [
        "record_id", "respondent_code", "role_code", "consent_status", "consent_form_id",
        "date", "duration_min", "mode", "question_id", "answer_summary", "probe",
        "critical_incident", "quote_id", "verbatim_anon", "external_use",
        "pair_id", "winner", "rank", "screen_id", "criterion", "pass", "observed", "pass_fail",
        "theme_match", "spend_evidence",
    ]
    missing_tpl = [f for f in required_fields if f not in template]
    check("G4", "template_field_schema", not missing_tpl, f"missing={missing_tpl}")
    has_dict = template.count("Allowed values / format") >= 6
    example_blocks = re.findall(r"```csv\n(.*?)```", template, re.S)
    check("G4", "template_value_dictionary", has_dict, "6 sections with type+allowed values columns")
    check("G4", "template_fictional_example_rows", len(example_blocks) == 6, f"{len(example_blocks)} example blocks")
    data_lines = [ln for ln in csv_text.splitlines() if ln and not ln.startswith("#")]
    header_names = set()
    for h in data_lines:
        first = h.split(",")[0]
        if first in {"record_id", "question_id", "quote_id", "pair_id", "screen_id", "criterion"}:
            header_names.update(h.split(","))
    missing_csv = [f for f in required_fields if f not in header_names]
    check("G4", "csv_headers_ready", not missing_csv, f"missing={missing_csv}")

    # G5: identity / bias scan across all package text files
    # banned words assembled from fragments so this source file never
    # contains the literals itself
    banned = ["place" + "holder", "lorem" + " ip" + "sum", "\u5360" + "\u4f4d", "clawhunt"]
    emails = re.compile(r"[\w.+-]+@[\w-]+\.[A-Za-z]{2,}")
    phones = re.compile(r"(\+\d{1,3}[\s-]?)?\d{3}-\d{3}-\d{4}|\(\d{3}\)\s?\d{3}-\d{4}")
    urls = re.compile(r"https?://")
    hits = []
    for p in sorted(ROOT.iterdir()):
        if p.suffix.lower() not in TEXT_SUFFIXES or p.name == Path(__file__).name:
            continue
        text = read(p)
        for b in banned:
            if b.lower() in text.lower():
                hits.append(f"{p.name}:banned:{b}")
        if emails.search(text):
            hits.append(f"{p.name}:email")
        if phones.search(text):
            hits.append(f"{p.name}:phone")
        if p.suffix != ".py" and urls.search(text):
            hits.append(f"{p.name}:url")
    check("G5", "identity_scan_zero_hits", not hits, f"hits={hits}")

    # G6: typography (ASCII quotes only)
    curly = [chr(c) for c in (0x2018, 0x2019, 0x201C, 0x201D)]
    curly_hits = []
    for p in sorted(ROOT.iterdir()):
        if p.suffix.lower() not in TEXT_SUFFIXES or p.name == Path(__file__).name:
            continue
        text = read(p)
        found = [ch for ch in curly if ch in text]
        if found:
            curly_hits.append(f"{p.name}:{''.join(found)}")
    check("G6", "ascii_quotes_only", not curly_hits, f"curly_hits={curly_hits}")

    # G7: every question carries purpose / flow / probe
    n_purpose = len(re.findall(r"- Purpose:", guide))
    n_flow = len(re.findall(r"- Flow:", guide))
    n_probe = len(re.findall(r"- Probe:", guide))
    check("G7", "every_question_has_purpose_flow_probe",
          n_purpose == 18 and n_flow == 18 and n_probe == 18,
          f"purpose={n_purpose} flow={n_flow} probe={n_probe}")

    # G8: cross-file screening enum consistency
    enum_tpl = "S2_activity_6mo" in template
    enum_scr = "S2_activity_6mo" in screening
    stale_variant = "S2_active_6mo" in (screening + template)
    check("G8", "screening_enum_consistent_across_files",
          enum_tpl and enum_scr and not stale_variant,
          f"template_has={enum_tpl} screening_has={enum_scr} stale_variant={stale_variant}")

    passed = CHECKS - len(FAILS)
    print(f"SUMMARY {passed}/{CHECKS} gates passed" + (" - ALL PASS" if not FAILS else f" - FAILED: {FAILS}"))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
