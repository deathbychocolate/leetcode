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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:  # break recursion
            return root

        # Invert left and right.
        left: TreeNode = root.left
        right: TreeNode = root.right
        root.left = right
        root.right = left

        self.invertTree(left)
        self.invertTree(right)

        return root


# Helper: convert Python list (level-order with None for missing nodes) to binary tree
def list_to_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list where None indicates a missing node.
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
        # Always enqueue children (possibly None) to preserve structure
        q.append(node.left)
        q.append(node.right)
    # Trim trailing None values
    while res and res[-1] is None:
        res.pop()
    return res


def run_test(input_list: List[Optional[int]], expected_list: List[Optional[int]], test_name: str) -> None:
    try:
        root = list_to_tree(input_list)
        inverted_root = Solution().invertTree(root)
        result = tree_to_list(inverted_root)
        ok = result == expected_list
        print(ok)
        if not ok:
            print(f"  input:    {input_list}")
            print(f"  expected: {expected_list}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"{test_name}: ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1], "Example 1"),
        ([2, 1, 3], [2, 3, 1], "Example 2"),
        ([], [], "Example 3 (empty)"),
        # Additional tests / edge cases
        ([1], [1], "Single node"),
        ([1, 2, None, 3], [1, None, 2, None, 3], "Left-skewed"),
        ([1, None, 2, None, 3], [1, 2, None, 3], "Right-skewed"),
        ([0, -2, 3], [0, 3, -2], "Negative values"),
        ([1, 2, 3, 4, None, None, 5], [1, 3, 2, 5, None, None, 4], "Mixed missing children"),
    ]

    for inp, expected, name in samples:
        run_test(inp, expected, name)


if __name__ == "__main__":
    main()
