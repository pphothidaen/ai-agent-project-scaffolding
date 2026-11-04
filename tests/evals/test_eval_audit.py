"""Eval tests with ground truth for the 5-layer audit and base agent behavior."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Ground truth for the audit scorecard.
GROUND_TRUTH_AUDIT = {
    "expected_score": 12,
    "expected_total": 12,
    "expected_failed": [],
}

# Ground truth for basic agent behavior.
GROUND_TRUTH_AGENT = {
    "Sentinel": {
        "status": "completed",
        "agent": "Sentinel",
        "response_contains": "verify safety bounds",
    }
}


def test_audit_score_matches_ground_truth():
    result = subprocess.run(
        [sys.executable, "scripts/audit_5layer.py", str(ROOT), "--json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert data["score"] == GROUND_TRUTH_AUDIT["expected_score"]
    assert data["total"] == GROUND_TRUTH_AUDIT["expected_total"]
    failed = [item["name"] for item in data["items"] if not item["passed"]]
    assert failed == GROUND_TRUTH_AUDIT["expected_failed"]


def test_base_agent_behavior_matches_ground_truth():
    from src.agents.base import BaseAgent

    for name, expected in GROUND_TRUTH_AGENT.items():
        agent = BaseAgent(name=name)
        result = agent.run("verify safety bounds")
        assert result["status"] == expected["status"]
        assert result["agent"] == expected["agent"]
        assert expected["response_contains"] in result["response"]
