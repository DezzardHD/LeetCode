class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l, r = 0, len(s)-1
        while True:
            if l > r:
                return 1
            if s[l] != s[r]:
                break
            l += 1
            r -= 1
        return 2