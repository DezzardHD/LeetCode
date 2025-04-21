class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for val in range(n + 1):
            ans.append(bin(val).count("1"))
        return ans
            
