class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        stk = []
        maxones = 0
        count = 0
        
        for i in nums:
            if i == 1:
                stk.append(i)
            else:
                if count < k:
                    stk.append(i)
                    count += 1
                else:
                    maxones = max(maxones, len(stk))
                    z = 1
                    while(stk and stk[0] != 0):
                        z = stk.pop(0)
                    if stk and stk[0] == 0:
                        z = stk.pop(0)
                    if z == 0:
                        count -= 1
                    if count < k:
                        stk.append(i)
                        count += 1
        return max(maxones, len(stk))
