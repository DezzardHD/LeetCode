class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for val in range(1, n + 1):
            print(val)
            if val % 3 == 0 and val % 5 == 0:
                res.append("FizzBuzz")
            elif val % 3 == 0:
                res.append("Fizz")
            elif val % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(val))
        return res