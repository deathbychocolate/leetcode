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
3. **Helper functions**: `list_to_tree()`, `list_to_linked()`, `linked_to_list()` for test case conversion (when needed)
4. **`run_test()` function**: Helper that executes a single test case with error handling
5. **`main()` function**: Contains a `samples` list of test cases and iterates through them
6. **`if __name__ == "__main__": main()`** guard

## Modern Pattern (Recent Solutions)

Recent solutions follow this pattern (see `78_subsets/main.py` or `100_same_tree/main.py`):

```python
class Solution:
    def methodName(self, param: list[int]) -> list[int]:
        # implementation
        pass

def run_test(input_params, expected):
    try:
        result = Solution().methodName(input_params)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  input:    {input_params}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"ERROR -> {e}")

def main() -> None:
    samples = [
        # Problem examples
        (input1, expected1),
        (input2, expected2),
        # Additional tests / edge cases
        (edge_case1, expected_edge1),
    ]

    for input_val, expected in samples:
        run_test(input_val, expected)

if __name__ == "__main__":
    main()
```

## Type Hints

**Use modern Python type hints (Python 3.9+):**
- Use `list[int]` instead of `List[int]` (no import needed)
- Use `dict[str, int]` instead of `Dict[str, int]` (no import needed)
- Use `Type | None` instead of `Optional[Type]` (union syntax)
- Only import from `typing` when needed for special types (e.g., `from collections import deque`)

## Test Output

Running a solution prints `True` for each passing test case and `False` (with detailed failure info) for failures. Exceptions are caught and printed with `ERROR ->` prefix.
