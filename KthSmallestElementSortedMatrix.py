class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0
        for i in matrix[1:]:
            matrix[0] += i
        return sorted(matrix[0])[k - 1]
