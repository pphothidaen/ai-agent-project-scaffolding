---
name: ai-sdlc-develop
description: Guides autonomous agents through the TDD-first Software Development Life Cycle within this harness.
---

# AI SDLC Development Skill

## Guidelines
1. **Red Stage**: Author a failing unit or evaluation test in `tests/`.
2. **Green Stage**: Write minimal production code under `src/` to make the test pass.
3. **Refactor Stage**: Improve code readability, typing, and docstrings without breaking tests.
4. **Gate Verification**: Run `python scripts/tdd_gate.py` to ensure gates pass before committing.

