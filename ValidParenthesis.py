class Solution:
    def isValid(self, s: str) -> bool:
        k = []
        dic = {'{':'}', '[':']', '(':')'}
        opene = ['{', '[', '(']
        close = ['}', ']', ')']
        
        for i in range(len(s)):
            if s[i] in opene:
                k.append(s[i])
            elif s[i] in close:
                if len(k)==0:
                    return False
                if dic[k[-1]] != s[i]:
                    print(dic[k[-1]], s[i])
                    return False
                else:
                    k.pop()
        if len(k) != 0:
            return False
        return True
