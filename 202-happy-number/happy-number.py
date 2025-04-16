class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set([n])
        while True:
            if n == 1:
                return True
            tmp = 0
            for val in str(n):
                tmp += int(val)**2
            if tmp in visited:
                return False
            visited.add(tmp)
            n = tmp
        
        