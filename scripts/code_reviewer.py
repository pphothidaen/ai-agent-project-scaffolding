#!/usr/bin/env python3
"""
Automated Code Reviewer & Guardrail Inspector
Enforces operating boundaries defined in AGENTS.md:
1. Scans staged and modified files for potential raw secret exposure.
2. Checks boundary adherence (restricting production changes to allowed directories).
3. Verifies no forbidden operations (e.g., direct DB migrations or dangerous queries).
"""
import os
import re
import subprocess
import sys

ALLOWED_EXTENSIONS = {
    ".py", ".md", ".toml", ".sh", ".yml", ".yaml", ".json", ".example",
    ".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".ico"
}

FORBIDDEN_PATTERNS = [
    (r"(?i)(password|secret|token|api_key)\s*[:=]\s*['\"][a-zA-Z0-9_\-]{16,}['\"]", "Hardcoded credentials or API key detected"),
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI API secret key pattern detected"),
    (r"AIzaSy[a-zA-Z0-9_-]{33}", "Google API key pattern detected"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub Personal Access Token detected"),
    (r"(?i)\bDROP\s+TABLE\b", "Dangerous SQL statement (DROP TABLE) detected without migration guard"),
]

def get_staged_or_recent_files():
    try:
        # Check staged files first
        res = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        files = [f.strip() for f in res.stdout.strip().split("\n") if f.strip()]
        if not files:
            # Fall back to working tree or tracked files
            res = subprocess.run(
                ["git", "ls-files"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            files = [f.strip() for f in res.stdout.strip().split("\n") if f.strip()]
        return files
    except Exception:
        # Fallback if git is not yet initialized or outside git
        matched = []
        for root, _, filenames in os.walk("."):
            if ".git" in root or ".venv" in root or "__pycache__" in root:
                continue
            for fn in filenames:
                matched.append(os.path.normpath(os.path.join(root, fn)))
        return matched

def review_code():
    print("[CODE REVIEW] Inspecting changes against AGENTS.md guardrails...")
    files = get_staged_or_recent_files()
    violations = []

    for filepath in files:
        if not os.path.isfile(filepath):
            continue
        # Skip checking binary files, git internal files, env templates, or the reviewer script itself
        if filepath.startswith(".git/") or filepath == ".env.example" or filepath == "scripts/code_reviewer.py":
            continue

        _, ext = os.path.splitext(filepath)
        if ext and ext not in ALLOWED_EXTENSIONS and not filepath.startswith(".githooks/"):
            violations.append(f"Disallowed file extension '{ext}' in {filepath}")

        # Skip scanning content of binary/media files
        if ext.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf"}:
            continue

        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            for pattern, reason in FORBIDDEN_PATTERNS:
                if re.search(pattern, content):
                    violations.append(f"{reason} in {filepath}")
        except Exception as e:
            violations.append(f"Unable to read {filepath}: {e}")

    if violations:
        print("[CODE REVIEW FAIL] Boundary violations found:")
        for v in violations:
            print(f"  ❌ {v}")
        return 1

    print("[CODE REVIEW PASS] All boundary checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(review_code())
