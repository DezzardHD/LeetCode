class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        res = [100000] * len(s)
        for i, val in enumerate(s):
            if val == c:
                res[i] = 0
                print('a')

                idx = i - 1
                while idx >= 0 and ((res[idx] == 100000 or res[idx] > i - idx) and s[idx] != c):
                    res[idx] = i - idx
                    idx -= 1
                idx = i + 1
                while idx < len(s) and ((res[idx] == 100000 or res[idx] > idx - i) and s[idx] != c):
                    res[idx] = idx - i
                    idx += 1
        return res