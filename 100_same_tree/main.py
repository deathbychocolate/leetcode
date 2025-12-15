from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class Solution:
    def dfs(self, t1: TreeNode | None, t2: TreeNode | None) -> bool:

        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False

        equal_val = t1.val == t2.val
        equal_left = self.dfs(t1=t1.left, t2=t2.left)
        equal_right = self.dfs(t1=t1.right, t2=t2.right)
        equal = equal_val and equal_left and equal_right
        return equal

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return self.dfs(t1=p, t2=q)


# Helper: convert Python list (level-order with None for missing nodes) to binary tree
def list_to_tree(values: list[int | None]) -> TreeNode | None:
    """
    Build a binary tree from a level-order list where None indicates a missing node.
    Example: [1,2,3,None,4] -> root with left child 2, right child 3, and 2's right child 4.
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


def run_test(p_values: list[int | None], q_values: list[int | None], expected: bool) -> None:
    try:
        p = list_to_tree(p_values)
        q = list_to_tree(q_values)
        result = Solution().isSameTree(p, q)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  p:        {p_values}")
            print(f"  q:        {q_values}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        # Additional tests / edge cases
        ([], [], True),
        ([1], [], False),
        ([1], [1], True),
        ([1, 2, None, 3], [1, 2, None, 3], True),
        ([1, None, 2, None, 3], [1, None, 2, None, 3], True),
        ([0, -2, 3], [0, -2, 3], True),
        ([1, 2, 3, 4], [1, 2, 3, None, 4], False),
    ]

    for p_vals, q_vals, expected in samples:
        run_test(p_vals, q_vals, expected)


if __name__ == "__main__":
    main()
