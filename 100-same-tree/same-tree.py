# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        self.explore(p, q)
        return self.res

    def explore(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> None:
        if not (node1 and node2):
            if (node1 == None) ^ (node2 == None):
                self.res = False
            return

        if node1.val != node2.val:
            self.res = False
            return
        
        self.explore(node1.left, node2.left)
        self.explore(node1.right, node2.right)