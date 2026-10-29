#!/usr/bin/env python3
"""Map a lawfully obtained source CSV to the study-local external record IDs.

This script never downloads or redistributes source text. The user supplies a
source CSV obtained under the source repository's terms. Matching uses the
SHA-256 digest of the exact UTF-8 text stored in the source CSV.
"""
import argparse
import csv
import hashlib
from pathlib import Path


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("source_csv", type=Path)
parser.add_argument("--source", required=True, choices=["rubend_jailbreak", "dolly_ood"])
parser.add_argument("--text-column", default=None)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()

root = Path(__file__).resolve().parents[1]
manifest_path = root / "evidence" / "00_frozen_screen_source" / "results" / "external_predictions.csv"
with manifest_path.open(encoding="utf-8-sig", newline="") as f:
    required = [r for r in csv.DictReader(f) if r["source"] == args.source]

with args.source_csv.open(encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = list(reader.fieldnames or [])

if "source" in fields:
    filtered = [r for r in rows if r.get("source") == args.source]
    if filtered:
        rows = filtered

if args.text_column:
    text_column = args.text_column
else:
    candidates = ["Prompt", "prompt", "text", "instruction"]
    text_column = next((c for c in candidates if c in fields), None)
if text_column is None or text_column not in fields:
    raise SystemExit("Specify --text-column. Available columns: " + ", ".join(fields))

by_hash = {}
for index, row in enumerate(rows, start=2):
    value = row.get(text_column, "")
    by_hash.setdefault(digest(value), []).append(index)

out = []
missing = []
for record in required:
    matches = by_hash.get(record["text_sha256"], [])
    if not matches:
        missing.append(record["study_record_id"])
    out.append({
        "study_record_id": record["study_record_id"],
        "source": record["source"],
        "text_sha256": record["text_sha256"],
        "source_csv_row_numbers": ";".join(str(i) for i in matches),
        "match_count": len(matches),
    })

args.output.parent.mkdir(parents=True, exist_ok=True)
with args.output.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(out[0]))
    writer.writeheader()
    writer.writerows(out)

if missing:
    raise SystemExit(f"Mapping incomplete. Missing {len(missing)} study records: " + ", ".join(missing[:10]))
print(f"PASS: mapped {len(out)} study records using exact SHA-256 matches")
