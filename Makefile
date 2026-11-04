PYTHON ?= python3

.PHONY: help init test check metrics clean

help:
	@echo "Available make commands:"
	@echo "  make init      - Configure git hooks and install development dependencies"
	@echo "  make check     - Run code review boundary checks, TDD gates, and metrics"
	@echo "  make test      - Run test suite"
	@echo "  make metrics   - Collect and display SDLC metrics"
	@echo "  make clean     - Clean python bytecode and cache files"

init:
	git config core.hooksPath .githooks
	chmod +x .githooks/* scripts/*.py bootstrap.sh
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) scripts/tdd_gate.py

check:
	$(PYTHON) scripts/code_reviewer.py
	$(PYTHON) scripts/tdd_gate.py
	$(PYTHON) scripts/ai_sdlc_metrics.py

metrics:
	$(PYTHON) scripts/ai_sdlc_metrics.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
