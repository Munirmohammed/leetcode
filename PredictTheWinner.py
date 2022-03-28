from collections import defaultdict


class Solution:
    def PredictTheWinner(self, nums):
       
        l = len(nums)
        gross = [0]  # sum [0:i]
        for e in nums:
            gross.append(gross[-1] + e)

        F = defaultdict(lambda: defaultdict(int))
        for i in range(l-1, -1, -1):
            for j in range(i+1, l+1):
                F[i][j] = max(
                    gross[j] - gross[i] - F[i+1][j],
                    gross[j] - gross[i] - F[i][j-1]
                )
        return F[0][l] >= (gross[-1] - F[0][l])


if __name__ == "__main__":
    assert Solution().PredictTheWinner([1, 5, 2]) == False
    assert Solution().PredictTheWinner([1, 5, 233, 7]) == True
