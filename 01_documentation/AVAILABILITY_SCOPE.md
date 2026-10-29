# Availability and verification scope

Included: the analysis notebook; de-identified authored workload definitions; sanitized external-prediction records; the fitted screening artifact; ordered feature columns; frozen row-level outcomes; derived analysis records; gate self-tests; annotation instruments; de-identified judgments; adjudication outcomes; environment records; table and figure mappings; source manifests; redaction audit; and package-wide checksums.

The external-prediction file contains no raw third-party text. It retains study-local record identifiers, source labels, SHA-256 hashes, labels, frozen predictions and correctness indicators. Indirect workloads, model-response files and annotation materials have been redacted where they contained or reproduced text from the unlicensed jailbreak collection. Derived labels, scores, decisions and judgments remain unchanged.

The train, validation and test splits contain records from sources with declared licences, as documented in `THIRD_PARTY_SOURCE_MANIFEST.csv`. The original source hash ledger remains available for provenance. Its external-prediction hash identifies the pre-redaction frozen input and is not expected to match the sanitized distributed file.

The package supports verification of the reported frozen results. Re-execution from third-party source text requires obtaining that text from the original repositories under their terms.
