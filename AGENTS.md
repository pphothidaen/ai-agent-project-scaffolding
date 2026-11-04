# AGENTS.md - Root Gateway for Autonomous Agents

## 1. Operating Boundaries
- **Environment**: Staging / Isolated Sandbox only.
- **Model Constraints**: Default to strict structured output (JSON schema/Pydantic).
- **Prohibited Actions**: Direct DB migrations, raw secret exposure, modification of files outside `src/` and `tests/`.
- **Boundary (Deep/Surface)**: Deep Layer (arch, data model, auth, deps, concurrency, migrations) → human PR merge; Surface Layer (impl, tooling, evals, telemetry) → AI autonomous with CI gates. See `.agents/rules/deep-surface-boundary.md`.

## 2. Risk-Tiering & Approvals
- **Tier 1 (Autonomous)**: Formatting, unit test generation, doc updates.
- **Tier 2 (Audit Log)**: Core logic implementation conforming to existing ADRs.
- **Tier 3 (HITL Required)**: Infrastructure changes, schema updates, third-party API mutations.

