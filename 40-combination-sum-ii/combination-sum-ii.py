class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def explore(idx: int, current: List[int], value: int):
            nonlocal target, candidates
            if target == value:
                res.append(current.copy())
                return
            if len(candidates) <= idx or target < value:
                return

            current.append(candidates[idx])
            explore(idx + 1, current, value + candidates[idx])
            current.pop()
            
            tmp_idx = idx + 1
            while tmp_idx < len(candidates) and candidates[tmp_idx] == candidates[idx]:
                tmp_idx += 1
            explore(tmp_idx, current, value)

        explore(0, [], 0)
        return res