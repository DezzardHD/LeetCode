# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.depth(root)
        return self.res

    def depth(self, node: Optional[TreeNode]) -> int:
        if not node or not self.res:
            return 0
        
        left = self.depth(node.left)
        right = self.depth(node.right)
        
        if abs(left-right) > 1:
            self.res = False
        
        return max(left + 1, right + 1)