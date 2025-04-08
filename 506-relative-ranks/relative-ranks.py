class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [(value, index) for index, value in enumerate(score)]
        score.sort()
        res = [0] * len(score)
        print(score)
        print(res)
        for i in range(len(score) - 1, -1, -1):
            if len(score) - i < 4:
                if len(score) - i == 1:
                    res[score[-1][1]] = "Gold Medal"
                elif len(score) - i == 2:
                    res[score[-2][1]] = "Silver Medal"
                elif len(score) - i == 3:
                    res[score[-3][1]] = "Bronze Medal"
                continue
            res[score[i][1]] = str(len(score) - i)
        return res