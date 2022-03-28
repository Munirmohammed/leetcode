class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            if n < 0:
                if n%2 == 0:
                    return self.myPow(x, n / 2) ** 2
                else:
                    return (1/x) * self.myPow(x, (n+1) / 2) ** 2
            else:
                if n%2 == 0:
                    return self.myPow(x, n / 2) ** 2
                else:
                    return x * self.myPow(x, (n-1) / 2) ** 2
