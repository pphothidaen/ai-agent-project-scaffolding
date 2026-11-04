#!/usr/bin/env python3
"""
TDD Gatekeeper:
Ensures agent generated verifiable tests and tests pass before commit / push.
1. Confirms test structure exists in tests/unit/ and tests/evals/.
2. Executes test suite (via pytest if available, falling back to unittest discovery).
"""
import os
import subprocess
import sys

def check_test_files():
    has_tests = False
    for root, _, files in os.walk("tests"):
        for f in files:
            if f.startswith("test_") and f.endswith(".py"):
                has_tests = True
                break
        if has_tests:
            break
    return has_tests

def run_tests():
    # Try pytest first
    try:
        import pytest  # noqa: F401
        res = subprocess.run([sys.executable, "-m", "pytest", "tests", "-v"], check=False)
        return res.returncode
    except ImportError:
        # Fall back to standard library unittest
        print("[TDD GATE] pytest not found in current python environment. Running unittest fallback...")
        res = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], check=False)
        return res.returncode

def verify_tdd_flow():
    print("[TDD GATE] Verifying test assertions and execution gates...")

    if not os.path.isdir("tests"):
        print("❌ [TDD GATE FAIL] 'tests/' directory not found.")
        return 1

    if not check_test_files():
        print("❌ [TDD GATE FAIL] No test files matching 'test_*.py' found in tests/. Fail-closed: tests required before commit.")
        return 1

    code = run_tests()
    if code != 0:
        print("❌ [TDD GATE FAIL] Tests failed. Fix assertions before proceeding.")
        return code

    print("✅ [TDD GATE PASS] All tests passed.")
    return 0

if __name__ == "__main__":
    sys.exit(verify_tdd_flow())
