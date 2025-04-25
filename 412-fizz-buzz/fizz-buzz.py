class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for val in range(1, n + 1):
            print(val)
            tmp = ""
            if val % 3 == 0:
                tmp += "Fizz"
            if val % 5 == 0:
                tmp += "Buzz"
            if tmp == "":
                res.append(str(val))
            else:
                res.append(tmp)
        return res