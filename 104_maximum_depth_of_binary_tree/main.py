# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth_left = 1
        depth_right = 1
        depth_left += self.maxDepth(root=root.left)
        depth_right += self.maxDepth(root=root.right)
        return max(depth_left, depth_right)

def main() -> None:
    # Input: root = [3,9,20,null,null,15,7]
    # Output: 3
    root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    result = Solution().maxDepth(root=root)
    print(result)

if __name__=="__main__":
    main()
