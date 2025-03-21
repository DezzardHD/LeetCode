# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        
        queue = deque([root])
        while queue:
            for _ in range(0, len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if self.isSameTree(node, subRoot):
                    return True
        return False

    def isSameTree(self, root: Optional[TreeNode], subtree: Optional[TreeNode]) -> bool:
        if not subtree and not root:
            return True
        if (root == None) ^ (subtree == None):
            return False
        if root.val != subtree.val:
            return False
        return self.isSameTree(root.left, subtree.left) and self.isSameTree(root.right, subtree.right)