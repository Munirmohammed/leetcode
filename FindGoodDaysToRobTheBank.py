class Solution(object):
    def goodDaysToRobBank(self, s, time):
        l=len(s)
        if l<2*time:return []
        
        ldc=[1]*l
        lic=[1]*l
        ans=[]
        for i in range(1,l):
            if s[i]<=s[i-1]:
                ldc[i]=ldc[i-1]+1
                
        for i in range(l-2,-1,-1):
            if s[i]<=s[i+1]:
                lic[i]=lic[i+1]+1
                
        for i in range(time,l-time):
            if ldc[i]>time and lic[i]>time:
                ans.append(i)
        return ans
