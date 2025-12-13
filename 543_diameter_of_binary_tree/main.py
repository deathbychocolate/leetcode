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
    def __init__(self):
        self._diameter = 0  # stores the maximum diameter calculated

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth_left = self.maxDepth(root=root.left) if root.left else 0
        depth_right = self.maxDepth(root=root.right) if root.right else 0
        self._diameter = max(self._diameter, depth_left + depth_right)

        return 1 + max(depth_left, depth_right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            self.maxDepth(root)
        return self._diameter


# Helper: convert Python list (level-order with None for missing nodes) to binary tree
def list_to_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list where None indicates a missing node.
    Example: [1,2,3,4,5] corresponds to the tree used in the problem examples.
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
        result = Solution().diameterOfBinaryTree(root)
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
        ([1, 2, 3, 4, 5], 3, "Example 1"),
        ([1, 2], 1, "Example 2"),
        # Additional tests / edge cases
        ([], 0, "Empty tree (no nodes)"),
        ([1], 0, "Single node (diameter 0)"),
        ([1, 2, None, 3], 2, "Left-skewed (3 nodes -> diameter 2)"),
        ([1, None, 2, None, 3], 2, "Right-skewed (3 nodes -> diameter 2)"),
        # Chain of 4 nodes -> diameter 3
        ([1, 2, None, 3, None, 4], 3, "Long left-leaning chain"),
        # Perfect tree of height 3 (levels 0..2) -> diameter 4 edges
        ([1, 2, 3, 4, 5, 6, 7], 4, "Perfect tree depth 3"),
        # Mixed missing children; longest path between leaf 4 and 5 through root
        ([1, 2, 3, 4, None, None, 5], 4, "Mixed missing children"),
        ([0, -2, 3, None, None, None, 4], 3, "Negative values and deeper right leaf"),
        # Subtree has longest diameter; does not pass through root
        ([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2], 8, "Longest diameter found in subtree"),
    ]

    for inp, expected, name in samples:
        run_test(inp, expected, name)


if __name__ == "__main__":
    main()
