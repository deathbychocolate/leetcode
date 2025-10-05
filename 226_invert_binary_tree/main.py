# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root

        # invert left and right
        left: TreeNode = root.left
        right: TreeNode = root.right
        root.left = right
        root.right = left

        self.invertTree(left)
        self.invertTree(right)

        return root

def main() -> None:
    # Input: root = [4,2,7,1,3,6,9]
    # Output: [4,7,2,9,6,3,1]
    root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)))
    print("BEFORE")
    print("========================================================")
    print(root.val, root.left.val, root.right.val)
    print(root.right.val, root.right.left.val, root.right.right.val)
    print(root.left.val, root.left.left.val, root.left.right.val)
    print()

    Solution().invertTree(root=root)
    print("AFTER")
    print("========================================================")
    print(root.val, root.left.val, root.right.val)
    print(root.right.val, root.right.left.val, root.right.right.val)
    print(root.left.val, root.left.left.val, root.left.right.val)
    print()

if __name__=="__main__":
    main()
