# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.result = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            depth_left = maxDepth(root=root.left)
            depth_right = maxDepth(root=root.right)
            self.result = max(self.result, depth_left + depth_right)
            return 1 + max(depth_left, depth_right)

        maxDepth(root=root)

        return self.result

def main() -> None:
    # Input: root = [1,2,3,4,5]
    # Output: 3
    # Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
    root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)), right=TreeNode(val=3))
    result = Solution().diameterOfBinaryTree(root=root)
    print(result)

if __name__=="__main__":
    main()
