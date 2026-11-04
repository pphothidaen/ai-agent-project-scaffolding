# Rule: Deep vs Surface Layer Boundary

> Scope: all changes

## Deep Layer (human PR merge)
Architecture, data model, auth, dependencies, concurrency, migrations.
AI may propose; human reviews and merges.

## Surface Layer (AI autonomous w/ CI gates)
Implementation, tooling, evals, telemetry.
AI may ship autonomously when all guardrails/CI pass.

## Escalation
- Surface work touching Deep concerns → escalate; open PR, no auto-merge.
- Uncertain classification → treat as Deep.
- Record Phase-crossing decisions in docs/adr/.

## Trust Ladder
Observation → Recommendation → Proposal → Approved Execution → Full Autonomy.
Promotion is evidence-based, reversible, and logged.
