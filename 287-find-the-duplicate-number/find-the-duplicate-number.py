class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for val in nums:
            index = abs(val) - 1
            if nums[index] > 0:
                nums[index] = nums[index] * (-1)
            else:
                return abs(val)