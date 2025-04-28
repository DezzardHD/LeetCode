class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = str(bin(n))
        print(s)
        res = ""
        s = "0" * (32 + 2 - len(s)) + s[2::]
        for val in reversed(s):
            res += val
        
        return int(res, 2)