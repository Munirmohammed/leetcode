class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        stk = []
        curst = []
        ans = 0
        
        for i in fruits:
            if not stk:
                stk.append(i)
                curst.append(i)
            else:
                if len(curst) < 2:
                    stk.append(i)
                    curst.append(i)
                else:
                    if i in curst:
                        stk.append(i)
                    else:
                        ans = max(ans, len(stk))
                        while(len(set(stk)) > 1):
                            if len(stk) > 9000:
                                stk = []
                                stk.append(i)
                                break
                            stk.pop(0)
                        k = stk[0]
                        curst = [k]
                        curst.append(i)
                        stk.append(i)
        return max(ans, len(stk))
