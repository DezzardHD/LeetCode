# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.explore(root)
        return self.max_depth
    
    def explore(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0    # it is questionable to return a one for the base case
        depth_left = self.explore(root.left)
        depth_right = self.explore(root.right)

        if self.max_depth < depth_left + depth_right:
            self.max_depth = depth_left + depth_right
        
        max_depth = depth_left if depth_left > depth_right else depth_right

        return 1 + max_depth