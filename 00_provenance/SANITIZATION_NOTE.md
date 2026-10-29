# Sanitization and source hashes

The source archive included earlier redaction records covering external prompts, indirect workloads, responses and annotation materials. Those historical records are retained. Its README did not match its recorded checksum.

## Public-package correction

Two residual response values identified in the preceding review were located by SHA-256 of lowercased, whitespace-normalized response text. All 14 occurrences across 11 CSV files were replaced by explicit redaction markers. The exact affected paths, row numbers, digest values and mapped study-local source identifiers are recorded in `01_documentation/PUBLIC_RELEASE_REDACTION_AUDIT.csv`.

Every changed CSV was checked against the supplied archive: headers, record order, record counts and all non-response fields were preserved. No predictions, scores, routing decisions or annotation judgments were changed. The two targeted normalized response digests no longer occur in the CSV files.

This preparation did not repeat a full-source similarity audit because the original 79 prompt texts were not supplied in this archive. Earlier claims of zero residual source matches are historical claims, not independently recertified here. The targeted check is not a legal threshold or a guarantee that no other source-derived wording exists.

`frozen_source_hashes.csv` remains the immutable ledger of original pre-redaction inputs. Current package files have separate hashes in `08_checksums/SHA256SUMS.txt`. The checksum manifest excludes itself.
