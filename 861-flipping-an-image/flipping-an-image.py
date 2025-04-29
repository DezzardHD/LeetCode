class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for val in image:
            tmpList = []
            for digit in reversed(val):
                tmpList.append(0 if digit else 1)
            res.append(tmpList)
        
        return res