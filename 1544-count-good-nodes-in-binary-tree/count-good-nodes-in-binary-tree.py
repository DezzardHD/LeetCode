# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        res += self.explore(root)
        return res
    def explore(self, node: TreeNode) -> int:
        count = 0
        if node.left:
            if node.val <= node.left.val:
                count += 1
            else:
                node.left.val = node.val
            count += self.explore(node.left)
        if node.right:
            if node.val <= node.right.val:
                count += 1
            else:
                node.right.val = node.val
            count += self.explore(node.right)
        return count