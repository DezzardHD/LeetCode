class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        while n > 2:
            print(n)
            n = n / 2.0
        if n == 2:
            return True
        return False