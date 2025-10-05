# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return [True, 0]

            left = dfs(root=root.left)
            right = dfs(root=root.right)
            balanced = left[0] and right[0] and abs(left[1]) - abs(right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root=root)[0]

def main() -> None:
    # Input: root = [3,9,20,null,null,15,7]
    # Output: true
    root: TreeNode = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    result = Solution().isBalanced(root=root)
    print(result)
    # Input: root = [1,2,2,3,3,null,null,4,4]
    # Output: false
    root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=4))), right=TreeNode(val=2))
    result = Solution().isBalanced(root=root)
    print(result)

if __name__ == "__main__":
    main()
