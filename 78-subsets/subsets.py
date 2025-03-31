class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def explore(subset: List[int], idx: int):
            nonlocal res, nums
            if idx == len(nums):
                res.append(subset)
                return
            subset_left = subset
            subset_right = subset.copy()
            subset_right.append(nums[idx])
            explore(subset_left, idx + 1)
            explore(subset_right, idx + 1)
        explore([], 0)
        return res