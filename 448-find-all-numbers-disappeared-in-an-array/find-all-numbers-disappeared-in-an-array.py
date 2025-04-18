class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for val in nums:
            if val < 0:
                continue
            i = val - 1
            while 0 <= i < len(nums) and nums[i] > 0:
                next_idx = nums[i] - 1
                nums[i] = -1
                i = next_idx

        res = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
