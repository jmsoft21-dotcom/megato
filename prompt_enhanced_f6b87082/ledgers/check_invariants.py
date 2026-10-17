#!/usr/bin/env python3
"""Compare an original prompt with its enhanced version.

Usage: check_invariants.py ORIGINAL ENHANCED [--json]

Extracts Host-sealed value tokens from ORIGINAL and reports which are absent
from ENHANCED. STRICT categories must be fully preserved unless the rewrite
ledger justifies the removal; SOFT categories (block labels, snake_case words)
may change but every missing one must be justified.
"""
import json
import re
import sys

STRICT = {
    "sha256": r"\b[0-9a-f]{64}\b",
    "hexfloat": r"0x1\.[0-9a-f]+p[+-]\d+",
    "win_path": r"[A-Z]:\\[^\s'\"`;,)\]]+",
    "filename": r"\b[\w.\-]+\.(?:json|parquet|txt|md|py)\b",
    "number": r"(?<![\w.])\d+(?:\.\d+)?(?:e-?\d+)?(?![\w])",
    "backtick": r"`[^`\n]+`",
    "candidate_id": r"\b(?:I[0-9]|H[0-9]{2}|TH)_[A-Z0-9_]+\b",
    "quoted": r"\"[^\"\n]{3,200}\"",
}
SOFT = {
    "upper_snake": r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b",
    "snake_case": r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b",
}


def tokens(text, pattern):
    return sorted({t.rstrip(".") for t in re.findall(pattern, text)})


def number_ok(tok):
    # Small integers (0-99) are ubiquitous; track multi-digit and decimals.
    return "." in tok or "e" in tok or len(tok) >= 3


def main():
    orig_path, enh_path = sys.argv[1], sys.argv[2]
    as_json = "--json" in sys.argv
    orig = open(orig_path, encoding="utf-8").read()
    enh = open(enh_path, encoding="utf-8").read()
    report = {"original": orig_path, "enhanced": enh_path,
              "size": {"orig_chars": len(orig), "enh_chars": len(enh),
                       "orig_words": len(orig.split()), "enh_words": len(enh.split()),
                       "orig_est_tokens": round(len(orig) / 4),
                       "enh_est_tokens": round(len(enh) / 4),
                       "char_delta_pct": round(100 * (len(enh) - len(orig)) / len(orig), 1)},
              "strict_missing": {}, "soft_missing": {}}
    for name, pat in STRICT.items():
        toks = tokens(orig, pat)
        if name == "number":
            toks = [t for t in toks if number_ok(t)]
        missing = [t for t in toks if t not in enh]
        if missing:
            report["strict_missing"][name] = missing
    for name, pat in SOFT.items():
        missing = [t for t in tokens(orig, pat) if t not in enh]
        if missing:
            report["soft_missing"][name] = missing
    report["strict_missing_count"] = sum(len(v) for v in report["strict_missing"].values())
    report["soft_missing_count"] = sum(len(v) for v in report["soft_missing"].values())
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        s = report["size"]
        print(f"size chars {s['orig_chars']} -> {s['enh_chars']} ({s['char_delta_pct']}%), est tokens {s['orig_est_tokens']} -> {s['enh_est_tokens']}")
        print(f"strict_missing={report['strict_missing_count']} soft_missing={report['soft_missing_count']}")
        for k, v in report["strict_missing"].items():
            print(f"  STRICT {k}: {v}")
        for k, v in report["soft_missing"].items():
            print(f"  SOFT {k}: {v}")


if __name__ == "__main__":
    main()
