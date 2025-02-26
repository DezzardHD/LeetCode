class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        mid = floor((r - l) / 2) + l
        while l < r:
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
            if l == r and nums[l] == target:
                return l
            mid = floor((r - l) / 2) + l
        return -1