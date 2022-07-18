class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        for i in range(1, len(A)): # xrange -> range by Hiro
            A[i] += A[i - 1]
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, len(A)): # xrange -> range by Hiro
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res
