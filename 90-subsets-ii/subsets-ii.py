class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        def explore(idx, current):
            nonlocal res
            if idx == len(nums):
                return
            current.append(nums[idx])
            res.append(current.copy())
            explore(idx + 1, current)
            current.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            explore(idx + 1, current)
        explore(0, [])
        return res