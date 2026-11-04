#!/usr/bin/env python3
"""
AI SDLC Metrics Collector:
Aggregates key metrics on agent codebase health, test coverage density,
ADR records, and defined agent skills.
"""
import json
import os
import sys

def count_files(directory, extension=None):
    if not os.path.isdir(directory):
        return 0
    total = 0
    for root, _, files in os.walk(directory):
        for f in files:
            if extension is None or f.endswith(extension):
                total += 1
    return total

def collect_metrics():
    print("[METRICS] Collecting AI SDLC cycle metrics...")
    metrics = {
        "agents_skills_count": count_files(".agents", "SKILL.md"),
        "unit_tests_count": count_files("tests/unit", ".py") - 1, # minus __init__
        "eval_tests_count": count_files("tests/evals", ".py") - 1,
        "integration_tests_count": count_files("tests/integration", ".py") - 1,
        "adr_count": count_files("docs/adr", ".md"),
        "specs_count": count_files("docs/specs", ".md"),
        "src_modules_count": count_files("src", ".py"),
    }
    # Ensure non-negative
    for k, v in metrics.items():
        if v < 0:
            metrics[k] = 0

    print(json.dumps(metrics, indent=2))
    return metrics

if __name__ == "__main__":
    collect_metrics()
    sys.exit(0)
