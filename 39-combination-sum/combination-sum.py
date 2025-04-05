class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def explore(id, current, value):
            if value == target:
                res.append(current.copy())
                return
            if id >= len(candidates) or value > target:
                return
            
            current.append(candidates[id])
            explore(id, current, value + candidates[id])
            current.pop()
            explore(id + 1, current, value)
            return
        explore(0, [], 0)
        return res