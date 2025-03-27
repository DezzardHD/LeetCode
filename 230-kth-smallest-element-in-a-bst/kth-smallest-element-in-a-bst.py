# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.explore(root, k, 0)
        return self.res


    def explore(self, node: Optional[TreeNode], k, count) -> int:
        if not node or self.res:
            return count

        count = self.explore(node.left, k, count)
        
        count += 1
        if k == count:
            self.res = node.val
        
        count = self.explore(node.right, k, count)

        return count