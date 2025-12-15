from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class Solution:

    def is_identical(self, t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False

        return (t1.val == t2.val) and self.is_identical(t1=t1.left, t2=t2.left) and self.is_identical(t1=t1.right, t2=t2.right)


    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if subRoot is None:
            return True
        elif root is None:
            return False
        elif root.val == subRoot.val and self.is_identical(t1=root, t2=subRoot):
            return True

        return self.isSubtree(root=root.left, subRoot=subRoot) or self.isSubtree(root=root.right, subRoot=subRoot)


# Helper: convert Python list (level-order with None for missing nodes) to binary tree
def list_to_tree(values: list[int | None]) -> TreeNode | None:
    """
    Build a binary tree from a level-order list where None indicates a missing node.
    Example: [3,4,5,1,2] corresponds to:
          3
         / \
        4   5
       / \
      1   2
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
def tree_to_list(root: TreeNode | None) -> list[int | None]:
    if not root:
        return []
    res: list[int | None] = []
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


def run_test(root_vals: list[int | None], subroot_vals: list[int | None], expected: bool) -> None:
    try:
        root = list_to_tree(root_vals)
        subroot = list_to_tree(subroot_vals)
        result = Solution().isSubtree(root, subroot)
        ok = result == expected
        print(ok)
        if not ok:
            print("  root:     ", root_vals)
            print("  subRoot:  ", subroot_vals)
            print("  expected: ", expected)
            print("  got:      ", result)
    except Exception as e:
        print("ERROR ->", e)


def main() -> None:
    samples: list[tuple[list[int | None], list[int | None], bool]] = [
        # Problem examples
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
        # Additional tests / edge cases
        ([1], [1], True),                         # subRoot equals root (single node)
        ([1], [2], False),                        # different single nodes
        ([1, 2, 3], [2], True),                   # subtree is a single child
        ([1, 2, 3, 4, None, None, 5], [2, 4], True),  # subtree matches left branch
        ([1, 2, 3, 4], [2, None, 4], False),      # structure mismatch
        ([1, 1, 1, 1, None, 1], [1, 1], True),    # repeated values, ensure structure matters
        ([1,2,3,4,5,6,7,8], [2,4,5,8], True),     # larger case
    ]

    for root_vals, subroot_vals, expected in samples:
        run_test(root_vals, subroot_vals, expected)


if __name__ == "__main__":
    main()
