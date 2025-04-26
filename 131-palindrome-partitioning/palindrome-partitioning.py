class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(substring: str) -> bool:
            l, r = 0, len(substring) - 1
            while l < r:
                if substring[l] != substring[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def explore(substring: str, tmpList: List[str]):
            nonlocal res
            if len(substring) == 0:
                res.append(tmpList.copy())
                return

            i = 0
            while i < len(substring):
                if isPalindrome(substring[0:i+1]):
                    tmpList.append(substring[0:i+1])
                    explore(substring[i+1::], tmpList)
                    tmpList.pop()
                i += 1
        explore(s, [])
        return res