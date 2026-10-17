#!/usr/bin/env python3
"""Independent acceptance checks for the enhanced Triopus prompts (design.md section 8 subset)."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ORIG = Path("/home/user/megato/prompt_originals_f6b87082")
ENH = Path("/home/user/megato/prompt_enhanced_f6b87082")
WD = Path(__file__).resolve().parent

EXPECTED_ORIG = {
    "c1_1": "fdb46d0be8e0d186064b05e0fef89030747b965a67451a5eb4f0ecce21e7dbf3",
    "c1_2": "4b2520912abaa3fa6c25590ebdc06d5070d98fb65f0ee8ac1a6cc1c2deea4f44",
    "c1_3": "272d47ae61c9cc5e91b09a2b09a47737fdc1dbe5ea7ada67f623bf5095c1b4ab",
    "c1_4": "efc51a23bccfa0cc012d00e63348beaaa0720f6bedeaaaedf8810f31840a2742",
    "c1_5": "e03b9baeeaca29a34d311a15404dc692dc4a627d00a31d190b0283a3c841f626",
    "c2_1": "75198bf71504a075d90ec659f01cb826258d4253b3aafb28801913f95012e0cc",
    "c2_2": "c4d66983b079e0cee71e9130dfb741ead01e677709b2c4ea92f576f891038821",
    "c2_3": "5ad5caf7f79cb8d108432a281943e0723b07435e78a67cce177648c3d892dfcd",
    "c2_4": "03411dd5768e8b6a68dfccf93e925f2ea2f082a3b540dae44993c32104190728",
    "c2_5": "ec0abf0c4b719f7f317a46b77bd0cb5a3db7263b831943a0aa8e5576f82c0974",
}
ROLE_TABLE_SHA = "04af00996bf74eb25805f6c059dbe6ba2724aec342fb15352005ad9233f18591"

GROUPS = {
    "ALL": ["c1_1", "c2_1", "c1_2", "c2_2", "c1_3", "c2_3", "c1_4", "c2_4", "c1_5", "c2_5"],
    "LANES": ["c1_2", "c2_2", "c1_3", "c2_3", "c1_4", "c2_4"],
    "AB": ["c1_2", "c2_2", "c1_3", "c2_3"],
    "GM": ["c1_1", "c2_1", "c1_5", "c2_5"],
}
SHARED = {
    "ALL": ["PRECEDENCE_V1", "TRIOPLUS_RESEARCH_QUALITY_V1"],
    "LANES": ["LANE_EXECUTION_RULES_V1", "SHARED_METRIC_DATA_CONTRACT_V1", "LANE_OUTPUT_RULES_V1",
              "BACKTEST_MAX_HARDWARE", "HOST_CONTROL_PLANE_OWNERSHIP", "CAMPAIGN_GOAL_DIRECTIVE", "CONVERGENCE_V1"],
    "AB": ["HTS_BACKTEST_PROGRESS", "LANE_RESOURCE_SHARE_V1"],
    "GM": ["GM_EXECUTION_RULES_V1", "INDEX_USE_RULE_V1", "MULTIPLE_TESTING_GUARD_V1", "TRANSPORT_NON_INTERACTIVE",
           "HTS_BACKTEST_PROGRESS", "CONVERGENCE_V1", "HOST_OOS_MEMBERSHIP_PACKET"],
}
ALLOWED_NEW_NUMBERS = {"50", "12", "24", "16", "32", "8", "2", "5060"}
NUM_RE = re.compile(r"(?<![\w.])\d+(?:\.\d+)?(?:e-?\d+)?(?![\w])")


def files(root):
    return {p.name[:4]: p for p in sorted(root.glob("c[12]_[1-5]_*.txt"))}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def blocks(text):
    """label (first token of a block's first line) -> list of block texts."""
    out = {}
    for chunk in re.split(r"\n\s*\n", text):
        chunk = chunk.strip("\n")
        if not chunk:
            continue
        label = chunk.split("\n", 1)[0].split()[0] if chunk.split() else ""
        out.setdefault(label, []).append(chunk)
    return out


def design_fences():
    d = (WD / "design.md").read_text(encoding="utf-8")
    fences = re.findall(r"```text\n(.*?)\n```", d, flags=re.S)
    by_label = {}
    for f in fences:
        label = f.split("\n", 1)[0].split()[0] if f.split() else ""
        by_label.setdefault(label, []).append(f)
    return by_label


def main():
    res = {}
    o, e = files(ORIG), files(ENH)
    # A1 originals unchanged
    res["A1_originals_unchanged"] = all(sha(o[k]) == v for k, v in EXPECTED_ORIG.items()) and \
        sha(ORIG / "Triopus 모델 우선순위.txt") == ROLE_TABLE_SHA
    # A2 names
    res["A2_names_match"] = sorted(p.name for p in o.values()) == sorted(p.name for p in e.values())
    if not res["A2_names_match"]:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return
    # A3 checker
    a3 = {}
    for k in sorted(o):
        r = json.loads(subprocess.run([sys.executable, str(WD / "check_invariants.py"), str(o[k]), str(e[k]), "--json"],
                                      capture_output=True, text=True).stdout)
        a3[k] = {"strict": r["strict_missing_count"], "soft": r["soft_missing_count"],
                 "strict_tokens": r["strict_missing"], "chars": f'{r["size"]["orig_chars"]}->{r["size"]["enh_chars"]}',
                 "delta_pct": r["size"]["char_delta_pct"]}
    res["A3_A12_checker"] = a3
    # A4 c1/c2 static identity
    a4 = {}
    for role in "12345":
        oc1 = set(o[f"c1_{role}"].read_text(encoding="utf-8").splitlines())
        oc2 = set(o[f"c2_{role}"].read_text(encoding="utf-8").splitlines())
        ec1 = e[f"c1_{role}"].read_text(encoding="utf-8").splitlines()
        ec2 = e[f"c2_{role}"].read_text(encoding="utf-8").splitlines()
        only1 = [l for l in ec1 if l not in set(ec2) and l not in oc1]
        only2 = [l for l in ec2 if l not in set(ec1) and l not in oc2]
        a4[role] = {"non_slot_diff_c1": [l[:120] for l in only1], "non_slot_diff_c2": [l[:120] for l in only2]}
    res["A4_c1c2_identity"] = a4
    # A5 shared blocks identical within group, and equal to design fence when the fence label is unique
    fences = design_fences()
    a5 = {}
    eb = {k: blocks(p.read_text(encoding="utf-8")) for k, p in e.items()}
    for g, labels in SHARED.items():
        for lab in labels:
            texts = {}
            for k in GROUPS[g]:
                bl = eb[k].get(lab)
                texts[k] = None if not bl else hashlib.sha256(bl[0].encode()).hexdigest()[:12]
            vals = set(texts.values())
            entry = {"identical": len(vals) == 1 and None not in vals}
            if not entry["identical"]:
                entry["per_file"] = texts
            fl = fences.get(lab)
            if fl and len(fl) == 1 and eb[GROUPS[g][0]].get(lab):
                entry["equals_design_fence"] = eb[GROUPS[g][0]][lab][0] == fl[0]
            a5[f"{g}:{lab}"] = entry
    # FLOW_POSITION_V1 lines 1-3
    fp = {}
    for k in GROUPS["ALL"]:
        bl = eb[k].get("FLOW_POSITION_V1")
        fp[k] = None if not bl else hashlib.sha256("\n".join(bl[0].split("\n")[:3]).encode()).hexdigest()[:12]
    a5["ALL:FLOW_POSITION_V1[1-3]"] = {"identical": len(set(fp.values())) == 1 and None not in fp.values(), "per_file": fp}
    res["A5_shared_blocks"] = a5
    # A7 no authoring-assistant model ids
    a7 = []
    for k, p in e.items():
        for i, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if re.search(r"claude-opus-[0-9]|[Oo]pus[ -]?[0-9]", l):
                a7.append(f"{k}:{i}: {l[:100]}")
    res["A7_model_ids"] = a7
    # A8 no new numbers
    orig_nums = set()
    for p in list(o.values()) + [ORIG / "Triopus 모델 우선순위.txt"]:
        orig_nums |= set(NUM_RE.findall(p.read_text(encoding="utf-8")))
    a8 = {}
    for k, p in e.items():
        new = sorted(set(NUM_RE.findall(p.read_text(encoding="utf-8"))) - orig_nums - ALLOWED_NEW_NUMBERS)
        if new:
            a8[k] = new
    res["A8_new_numbers"] = a8
    # A15 markdown headings not present in originals
    a15 = {}
    for k, p in e.items():
        olines = set(o[k].read_text(encoding="utf-8").splitlines())
        bad = [l[:80] for l in p.read_text(encoding="utf-8").splitlines() if l.startswith("#") and l not in olines]
        if bad:
            a15[k] = bad
    res["A15_new_md_headings"] = a15
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
