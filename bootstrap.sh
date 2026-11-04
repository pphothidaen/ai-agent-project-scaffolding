#!/usr/bin/env bash
set -e

echo "🚀 Bootstrapping AI Agent Project Scaffolding..."

# 1. Activate Git hooks
git config core.hooksPath .githooks
chmod +x .githooks/*
echo "✅ Git hooks configured."

# 2. Check virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "💡 Recommendation: create a virtual environment (python -m venv .venv && source .venv/bin/activate)"
fi

# 3. Substitute PROJECT_NAME placeholder (portable: works on macOS and Linux)
if [ -n "${PROJECT_NAME:-}" ]; then
    echo "🔧 Substituting PROJECT_NAME='${PROJECT_NAME}'..."
    python3 -c "import os,sys; p=sys.argv[1]; s=open(p).read(); s=s.replace('PROJECT_NAME', os.environ['PROJECT_NAME']); open(p,'w').write(s)" AGENTS.md
    python3 -c "import os,sys; p=sys.argv[1]; s=open(p).read(); s=s.replace('PROJECT_NAME', os.environ['PROJECT_NAME']); open(p,'w').write(s)" docs/PROJECT.md
    echo "✅ PROJECT_NAME substituted."
fi

# 4. Make scripts executable
chmod +x scripts/*.py
echo "✅ Script permissions set."

# 5. Verify guardrails
python3 scripts/code_reviewer.py
python3 scripts/tdd_gate.py

echo "✅ Environment is ready for autonomous agent development!"
echo ""
echo "Next steps:"
echo "  1. Review AGENTS.md and docs/PROJECT.md for project-specific settings."
echo "  2. Create a virtual environment: python3 -m venv .venv && source .venv/bin/activate"
echo "  3. Install dependencies: pip install -e \".[dev]\""
echo "  4. Run guardrails: make check"
echo "  5. Start developing in src/ and tests/ with TDD-first workflow."
