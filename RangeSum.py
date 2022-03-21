class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = {}
        for row in range(len(self.matrix)):
            presums = []
            prev = 0
            for col in range(len(self.matrix[row])):
                presums.append(prev + self.matrix[row][col])
                prev = presums[-1]
            self.prefix[row] = presums
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            start, end = col1 - 1, col2
            if start < 0: 
                ans += (self.prefix[i][end])
            else:
                ans += (self.prefix[i][end] - self.prefix[i][start])
        return ans
