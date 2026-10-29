# Repository contents

## Documentation

- `README.md`: package purpose, verification scope and third-party text treatment.
- `RIGHTS_AND_ATTRIBUTION.md`: rights and source attribution notice.
- `01_documentation/TABLE_FIGURE_FILE_MAP.csv`: mapping from reported items to supporting files.
- `01_documentation/THIRD_PARTY_SOURCE_MANIFEST.csv`: source URLs, declared licences, uses and package treatment.
- `01_documentation/REDACTION_AUDIT.csv`: file-level record of source-text removal.
- `01_documentation/AVAILABILITY_SCOPE.md`: what can be verified directly and what requires lawful source access.

## Code

- `02_code/analysis_workflow.ipynb`: frozen analysis workflow. Text-dependent generation requires lawful source rehydration.
- `02_code/reconstruct_external_record_mapping.py`: maps lawfully obtained source CSV records to study-local IDs using exact SHA-256 hashes.

## Evidence

- `evidence/00_frozen_screen_source/results/train.csv`, `val.csv`, `test.csv`: byte-identical licensed-source screening splits.
- `evidence/00_frozen_screen_source/results/external_predictions.csv`: sanitized derived external records with no raw text.
- `evidence/00_provenance/external_record_hashes.csv`: study-local external record identifiers and SHA-256 hashes.
- `evidence/01_workloads/`: authored and sanitized workload definitions.
- `evidence/02_screen/`: reconstructed screen artifacts and verification records.
- `evidence/03_raw_models/`: frozen model outputs with source-derived text fields redacted where required.
- `evidence/04_analysis/`: derived analyses with source-derived text fields redacted where required.
- `evidence/05_annotation/`: annotation materials and outcomes with source-derived text fields redacted where required.
- `evidence/06_summary/`: headline result and integrity summaries.

## Integrity

- `08_checksums/SHA256SUMS.txt`: hashes of the distributed package files.
- `08_checksums/verify_checksums.py`: checksum verifier.
- `09_integrity/PREPARATION_LOG.csv`: preparation operations.
- `09_integrity/SOURCE_HASHES.txt`: hashes of original source-level inputs.

The original hash ledger in `evidence/00_provenance/frozen_source_hashes.csv` is retained as provenance. Its entry for `external_predictions.csv` records the pre-redaction source file. The distributed version is identified by the package-wide checksum manifest.
