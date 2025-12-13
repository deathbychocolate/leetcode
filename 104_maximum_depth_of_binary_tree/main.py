from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

    # Convenience for debugging when needed
    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:  # Base case: no root -> Depth is 0.
            return 0

        left: TreeNode | None = root.left
        right: TreeNode | None = root.right
        depth_left = 1
        depth_right = 1
        depth_left += self.maxDepth(left)
        depth_right += self.maxDepth(right)

        return max(depth_left, depth_right)


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


def run_test(input_list: List[Optional[int]], expected: int, test_name: str) -> None:
    try:
        root = list_to_tree(input_list)
        result = Solution().maxDepth(root)
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
        ([3, 9, 20, None, None, 15, 7], 3, "Example 1"),
        ([1, None, 2], 2, "Example 2"),
        # Additional tests / edge cases
        ([], 0, "Empty tree"),
        ([1], 1, "Single node"),
        ([1, 2, None, 3], 3, "Left-skewed"),
        ([1, None, 2, None, 3], 3, "Right-skewed"),
        ([0, -2, 3], 2, "Negative values"),
        # Balanced tree of depth 4
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, "Balanced depth 4 (partial)"),
        # Mixed missing children
        ([1, 2, 3, 4, None, None, 5], 3, "Mixed missing children"),
    ]

    for inp, expected, name in samples:
        run_test(inp, expected, name)


if __name__ == "__main__":
    main()