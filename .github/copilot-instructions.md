<!-- .github/copilot-instructions.md -->
# Copilot / AI Agent Instructions — blackjack-simulator

Purpose: quick, actionable guidance so an AI coding agent can be immediately productive in this repository.

- **Big picture**: this repo implements a small blackjack simulator library under `src/blackjack_sim`.
  - Core domain models live in `src/blackjack_sim/core` (cards, deck, hands).
  - Strategy implementations are intended to live in `src/blackjack_sim/strategies`.
  - Unit tests are under `tests/unit`.

- **Code style / patterns to follow**
  - Use `dataclasses` for simple domain objects and `IntEnum` for enumerations (see `src/blackjack_sim/core/card.py`).
  - Prefer explicit type hints (e.g., `list[int]`, return type annotations) — the codebase follows modern typing.
  - Enums implement `__str__` for human-readable symbols (suit symbols are used in `card.py`).
  - Keep changes minimal and focused: this repo is small and lacks a wide test surface.

- **Where to make changes**
  - Add core logic to `src/blackjack_sim/core/`.
  - Add new player strategies as modules under `src/blackjack_sim/strategies/`.
  - Add unit tests alongside existing tests in `tests/unit/` and name them `test_<module>.py`.

- **Build / test / debug**
  - Project uses a local virtual environment (if present, `.venv/`). Prefer activating it before installing deps.
  - Typical commands (run from repository root):
    - Install deps: `pip install -r requirements.txt` (file may be empty — add needed packages when required).
    - Run tests: `pytest -q tests/unit`.
    - Run a single test file: `pytest -q tests/unit/test_example.py`.

- **Repository-specific notes discovered**
  - `README.md` is currently empty — there's no high-level developer doc yet.
  - `.github/workflows/` exists but contains no workflows; assume no CI is configured.
  - `src/blackjack_sim/core/card.py` demonstrates the primary conventions for enums and dataclasses; refer to it when modelling new domain types.

- **Agent behavior rules (practical)**
  - Do not introduce large, cross-cutting refactors without a corresponding test update.
  - When adding functions or public APIs, include or update unit tests under `tests/unit/`.
  - If you change typing or signatures, update call sites and tests; prefer backward-compatible extensions.
  - If you need external dependencies, update `requirements.txt` and add installation instructions in the repository README.

- **Quick examples**
  - To model a new card-related object, mirror patterns in `src/blackjack_sim/core/card.py` (use `IntEnum`, `dataclass`, and typed properties).
  - When creating a strategy module, keep it self-contained and testable: a strategy module should expose its decision function and be covered by unit tests in `tests/unit/`.

If anything here is unclear or you want more detail about how strategies and the game loop communicate, tell me which file or API you want documented and I will iterate.
