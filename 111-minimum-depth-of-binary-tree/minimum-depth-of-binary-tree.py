# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([root])
        curr_depth = 1
        
        while queue:
            for _ in range(len(queue)):
                
                node = queue.popleft()
                if not node.left and not node.right:
                    return curr_depth
                
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
            curr_depth += 1