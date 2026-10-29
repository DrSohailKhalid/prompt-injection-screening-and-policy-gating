#!/usr/bin/env python3
import hashlib
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = root / "08_checksums" / "SHA256SUMS.txt"
failures = []
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    expected, relative = line.split("  ", 1)
    path = root / relative
    if not path.is_file():
        failures.append(f"MISSING {relative}")
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != expected:
        failures.append(f"MISMATCH {relative}")
if failures:
    print("\n".join(failures))
    raise SystemExit(1)
print("PASS: all repository files match SHA256SUMS.txt")
