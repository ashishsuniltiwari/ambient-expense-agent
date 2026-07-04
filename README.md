# Ambient Expense Agent (v2)

An autonomous, stateful, graph-based AI agent infrastructure built using the Google ADK (Agent Development Kit) framework. This agent intelligently evaluates, validates, and routes corporate expense transactions while enforcing strict local security gating.

## 🚀 Features

- **Stateful Routing Graph:** Tracks multi-turn transactional context to determine if expenses require manager evaluation or route automatically.
- **Deterministic Evaluation:** Automatically handles policy evaluations (e.g., auto-approving standard items under $100).
- **Security Interception Node:** Built-in verification nodes designed to detect and flag prompt injection risks or malicious override attempts.
- **Robust Local Testing:** Structured `pytest` unit suites ensuring predictable behavior inside isolated runtime pipelines.

## 🛠️ Architecture & Tech Stack

- **Framework:** Google ADK (Agent Development Kit)
- **Language & Runtime:** Python 3.13+ managed via `uv`
- **Testing Suite:** `pytest` with `pytest-asyncio` isolation
- **Security Boundaries:** Local `Semgrep` static analysis hooks

## 📦 Local Setup & Installation

Ensure you have the `uv` package manager installed on your workstation.

1. **Navigate to the Project:**
   ```powershell
   cd "C:\Users\Ashish Tiwari\Desktop\agy2-projects\ambient-expense-agent\expense-agent-v2"
2. **Install Project Dependencies:**
   ```powershell
   uv sync
3. **Run the Test Suite:**
Execute the local unit tests to verify proper agent graph configuration:
```powershell
uv run pytest tests/unit/


## 🛡️ Pre-Commit Security Gating

This repository utilizes local pre-commit hooks integrated with `Semgrep` to prevent sensitive credentials or vulnerable code patterns from being checked into version control.

To trigger a manual scan during staging:

```powershell
git add .
git commit -m "feat: run local security gates"

```

```

```
