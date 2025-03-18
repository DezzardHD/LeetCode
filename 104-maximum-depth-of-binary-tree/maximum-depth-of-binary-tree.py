# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.explore(root, 0)
        return self.max_depth

    def explore(self, node: Optional[TreeNode], curr_depth: int) -> Optional[TreeNode]:
        if not node:
            return None
        curr_depth += 1

        if self.max_depth < curr_depth:
            self.max_depth = curr_depth

        self.explore(node.left, curr_depth)
        self.explore(node.right, curr_depth)
        return None