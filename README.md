# Agent Safety: Computational Evidence

Repository authors: **Sohail** and **Quratulain Ali**.

Computational evidence accompanying research accepted in *Expert Systems with Applications*. This repository contains the analysis workflow, evaluation workloads, frozen model outcomes, annotation records and supporting provenance. Repository authorship is separate from the authorship of the associated article.

## Start here

1. Download or clone the repository.
2. From the repository root, check file integrity:

   ```bash
   python 08_checksums/verify_checksums.py
   ```

3. Read `01_documentation/TABLE_FIGURE_FILE_MAP.csv` to locate the evidence for individual tables and figures.
4. Read `01_documentation/AVAILABILITY_SCOPE.md` before running the notebook in `02_code/analysis_workflow.ipynb`.

The checksum verifier uses the Python standard library. The recorded experimental environment is in `evidence/00_provenance/environment_pip_freeze.txt`. The notebook is an archived workflow, not a one-command reproduction environment. Review its configurable input and output locations before execution and keep generated outputs outside the frozen evidence folders. Do not load the serialized model artifact from an untrusted or modified source.

## Contents

| Directory | Contents |
| --- | --- |
| `01_documentation/` | Scope, source manifest, file map and redaction records |
| `02_code/` | Analysis notebook and source-record mapping script |
| `evidence/` | Workloads, frozen predictions, model outputs, analyses and annotations |
| `08_checksums/` | SHA-256 manifest and verification script |
| `09_integrity/` | Preparation history and source integrity records |

## Source data and text redaction

The external-prediction table represents 79 jailbreak-source records and 183 Dolly records using study-local identifiers, hashes and frozen derived fields rather than raw source text. The source manifest documents dataset URLs, declared licences, study uses and treatment. Original dataset revision identifiers were not recorded in the frozen archive.

Source-derived passages identified during preparation have been redacted in workload, response and annotation artifacts. The public-package preparation additionally removed two known residual response values from all 14 identified CSV occurrences. See `01_documentation/PUBLIC_RELEASE_REDACTION_AUDIT.csv` and `evidence/00_provenance/SANITIZATION_NOTE.md` for the scope of these checks. Predictions, labels, routing decisions, scores and annotation judgments were preserved.

The frozen train, validation and test splits retain source text from OASST1, Dolly and Deepset. Their source attribution and declared terms are listed in `01_documentation/THIRD_PARTY_SOURCE_MANIFEST.csv` and `RIGHTS_AND_ATTRIBUTION.md`.

## Verification and re-execution

The saved derived evidence supports inspection and analysis of frozen outcomes. Re-execution of text-dependent predictions or model generations requires the relevant source text. `02_code/reconstruct_external_record_mapping.py` accepts a locally supplied source CSV and matches exact content hashes to study-local identifiers; it does not download source data. Use its `--help` option for arguments.

The pre-redaction hashes in `evidence/00_provenance/frozen_source_hashes.csv` are historical provenance. Current distributed files are identified separately in `08_checksums/SHA256SUMS.txt`. A checksum pass establishes file identity, not scientific validity or redistribution permission.

## Citation and rights

Repository citation metadata is supplied in `CITATION.cff`. Cite the associated article separately with its published author list. No blanket licence is assigned to this mixed-source package. See `RIGHTS_AND_ATTRIBUTION.md` for the distinction between authored materials and third-party source terms.
