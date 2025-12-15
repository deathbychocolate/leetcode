from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    # Convenience for debugging when needed
    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def max_depth(self, root: TreeNode | None) -> tuple[bool, int]:

        if root is None:
            return True, 0

        left = self.max_depth(root = root.left)
        right = self.max_depth(root = root.right)
        balanced: bool = left[0] and right[0] and abs(left[1] - right[1]) < 2

        return balanced, 1 + max(left[1], right[1])

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.max_depth(root=root)[0]


# Helper: convert Python list (level-order with None for missing nodes) to binary tree
def list_to_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list where None indicates a missing node.
    Example: [3,9,20,None,None,15,7] corresponds to the example tree.
    """
    if not values:
        return None
    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        try:
            left_val = next(it)
        except StopIteration:
            break
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        try:
            right_val = next(it)
        except StopIteration:
            break
        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)
    return root


# Helper: convert binary tree back to Python level-order list (trailing Nones trimmed)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    res: List[Optional[int]] = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            res.append(None)
            continue
        res.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while res and res[-1] is None:
        res.pop()
    return res


def run_test(input_list: List[Optional[int]], expected: bool, test_name: str) -> None:
    try:
        root = list_to_tree(input_list)
        result = Solution().isBalanced(root)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  input:    {input_list}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"{test_name}: ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        ([3, 9, 20, None, None, 15, 7], True, "Example 1"),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False, "Example 2"),
        ([], True, "Example 3 (empty)"),
        # Additional tests / edge cases
        ([1], True, "Single node"),
        ([1, 2, None, 3], False, "Left-skewed (unbalanced)"),
        ([1, None, 2, None, 3], False, "Right-skewed (unbalanced)"),
        ([1, 2, 3], True, "Root with two single children (balanced)"),
        ([1, 2, 2, 3, None, None, 3], True, "Subtree imbalance"),
        ([0, -2, 3, None, None, None, 4], True, "Negative values and deeper leaf on one side but balanced"),
        # Larger balanced tree
        ([1,2,3,4,5,6,7,8,9,10,11], True, "Larger balanced-ish tree"),
    ]

    for inp, expected, name in samples:
        run_test(inp, expected, name)


if __name__ == "__main__":
    main()
