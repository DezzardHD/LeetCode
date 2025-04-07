class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def explore(current: [int]):
            nonlocal res
            if len(current) == len(nums):
                res.append(current.copy())
                return
            i = 0
            while i < len(nums):
                if nums[i] == 11:
                    i += 1
                    continue
                current.append(nums[i])
                nums[i] = 11
                explore(current)
                nums[i] = current.pop()
                i += 1
        explore([])
        return res