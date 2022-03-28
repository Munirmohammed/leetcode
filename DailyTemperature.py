class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lis = [0] * len(temperatures)
        stack = []
        output = []
        for i, j in enumerate(temperatures):
            if not stack:
                stack.append([i,j])
            else:
                if stack[-1][1] >= j:
                    stack.append([i,j])
                else:
                    while(stack and stack[-1][1] < j ):
                        x = stack[-1][0] - i
                        lis[stack[-1][0]] = (-x)
                        stack.pop()
                    stack.append([i,j])
        return lis
