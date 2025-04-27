class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lookup = [None,None,["a","b","c"], ["d","e","f"], ["g","h","i"], ["j","k","l"], ["m","n","o"], ["p","q","r","s"], ["t","u","v"], ["w","x","y","z"]]
        res = []
        def explore(idx: int, current: str):
            nonlocal lookup, res
            if len(current) == len(digits):
                res.append(current)
                return

            digit = int(digits[idx])
            for val in lookup[digit]:
                explore(idx + 1, current + val)

        explore(0, "")
        return res