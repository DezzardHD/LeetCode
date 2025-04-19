# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def explore(left, right):
            mid = (right - left) // 2 + left
            if left > right:
                return None
            return TreeNode(nums[mid], explore(left, mid - 1), explore(mid + 1, right))
        return explore(0 ,len(nums) - 1)


