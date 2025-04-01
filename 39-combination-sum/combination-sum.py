class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        def create_key(combination: List[int]) -> dict[int, int]:
            a = {}
            for val in combination:
                a[val] = a.get(val, 0) + 1
            return a

        def explore(idx: int, value: int, current_list: List[int]):
            nonlocal res, nums, target
            if value == target:
                res.add(frozenset(create_key(current_list).items()))
                return
            if value > target:
                return
            for i in range(idx, len(nums)):
                tmp = value
                tmp += nums[i]
                tmp_list = current_list.copy()
                tmp_list.append(nums[i])
                explore(idx, tmp, tmp_list)
        for i in range(0, len(nums)):                
            explore(i, 0, [])
        
        real_res = []
        for hm in res:
            tmp = []
            for key, val in hm:
                tmp += [key] * val
            real_res.append(tmp)
        
        return real_res