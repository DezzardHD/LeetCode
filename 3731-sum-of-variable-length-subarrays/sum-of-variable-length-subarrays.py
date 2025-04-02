class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            res.append(sum(nums[start:i+1]))
        return sum(res)