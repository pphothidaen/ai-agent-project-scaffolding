# Rule: Review & Audit

> Scope: all changes pre-merge

## Requirements
1. Scan diffs for secret leakage and path violations.
2. Verify tests pass and guardrails green.
3. Validate AST/syntax and encoding integrity.
4. Enforce doc updates when architecture/features change.
5. Fail closed: no READY_FOR_PROD without all gates green.
