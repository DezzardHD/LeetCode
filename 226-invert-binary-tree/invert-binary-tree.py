# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # switch elements
        tmp = root.left if root.left else None
        root.left = root.right if root.right else None
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root