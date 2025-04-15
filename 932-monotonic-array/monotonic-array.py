class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_decreasing = True
        is_increasing = True
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                is_increasing = False
            if nums[i] < nums[i + 1]:
                is_decreasing = False
        
        return is_decreasing or is_increasing