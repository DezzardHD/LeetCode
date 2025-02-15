class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {value: index for index, value in enumerate(nums)}
        for index, value in enumerate(nums):
            searched_value = lookup.get(target - value)
            if(searched_value and searched_value != index):
                return [index, searched_value]