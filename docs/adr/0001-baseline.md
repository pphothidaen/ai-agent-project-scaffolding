# ADR 0001: Baseline Architecture & Boundaries

## Status
Accepted

## Context
Autonomous agents require strict boundary enforcement to prevent regressions, accidental environment pollution, and insecure operations.

## Decision
1. Enforce strict TDD flow via `scripts/tdd_gate.py` before merging changes.
2. Code generation is restricted to `src/` and test suites in `tests/`.
3. Agent operational skills are declared explicitly under `.agents/`.

## Consequences
- Deterministic and auditable agent changes.
- Safe automated development cycles.

