# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a LeetCode solutions repository containing Python solutions to various LeetCode problems. Each problem has its own directory.

## Directory Structure

Each solution follows the naming convention: `{problem_number}_{problem_name}/main.py`

Examples:
- `1_two_sum/main.py`
- `100_same_tree/main.py`
- `155_min_stack/main.py`

## Running Solutions

Each solution is a standalone Python file that can be run directly:

```bash
python {problem_number}_{problem_name}/main.py
```

Example:
```bash
python 1_two_sum/main.py
```

## Code Structure Pattern

Each `main.py` file typically contains:

1. **Data structure definitions** (when needed): `TreeNode`, `ListNode`, or custom classes like `MinStack`
2. **Solution class**: Contains the main algorithm method matching LeetCode's expected signature
3. **Helper functions**: `list_to_tree()`, `list_to_linked()`, `linked_to_list()` for test case conversion
4. **`main()` function**: Runs test cases and prints `True`/`False` for pass/fail
5. **`if __name__ == "__main__": main()`** guard

## Type Hints

Solutions use Python type hints (`List`, `Optional`, `TreeNode | None`, etc.). Import from `typing` module when needed.

## Test Output

Running a solution prints `True` for each passing test case and `False` (with details) for failures.
