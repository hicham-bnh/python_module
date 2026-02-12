<!-- .github/copilot-instructions.md: guidance for AI coding agents working in this repo -->
# Quick agent guide — python_module

Purpose
- This repository is a collection of small, self-contained Python exercises grouped under `python00/`..`python05/`.
- Each `pythonNN/exM/` directory contains one script/module that implements a focused task (naming convention: `ft_*` or short descriptive filenames).

Big picture
- Structure is intentionally flat: many independent examples rather than a single application. Treat each `ex*` module as an independent unit.
- Data flow is local to a file: functions take inputs and return outputs (scripts sometimes print). Example components:
  - `python05/ex0/stream_processor.py` defines an abstract `DataProcessor` and concrete processors.
  - `python00/ex5/ft_count_harvest_recursive.py` / `ft_count_harvest_iterative.py` show algorithmic function patterns.

How to run and iterate
- Run any exercise directly with the system Python: `python3 path/to/<file>.py` (workspace root is fine). Example:
  - `python3 python05/ex0/stream_processor.py`
- For unit-style work, import the module from a short script or REPL: `from python00.ex5 import ft_count_harvest_iterative` (or use path-based imports if you add an __init__.py).
- Debugging: use prints or run the file in the terminal. There is no test harness by default.

Repository conventions (explicit)
- File naming: helper/exercise functions are commonly prefixed with `ft_` (e.g., `ft_garden_intro.py`, `ft_seed_inventory.py`). Keep this pattern for new exercises.
- Prefer small, single-responsibility functions. If you add classes, ensure they are clearly tested or exercised by a runnable script.
- Typing appears in some files (e.g., `typing` and `abc` are used in `stream_processor.py`). Favor lightweight type hints for public functions.

Dependencies and integration
- No centralized dependency file found. If you add dependencies, add a `requirements.txt` at repo root and document the `python` version in the repo README.

PR / editing guidance
- Make small, focused changes to a single `ex*` folder. Avoid large cross-folder refactors unless you add tests and update the top-level README.
- If you create new modules intended for reuse, add an `__init__.py` in the containing folder and update a short README describing usage.

Files to inspect first (examples)
- `python05/ex0/stream_processor.py` — shows ABC usage and typing patterns.
- `python00/ex5/ft_count_harvest_iterative.py` and `ft_count_harvest_recursive.py` — algorithm examples.
- `python01/ex0/ft_garden_intro.py` — a typical small script showing I/O and simple logic.

When you are uncertain
- Prefer minimal, reversible edits. Run the module after change. If an edit affects many exercises, request human review.

If anything here is unclear or you want more examples (tests, a sample requirements.txt, or a README), ask and I will expand this file.
