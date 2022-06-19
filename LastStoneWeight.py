class Solution(object):
   def lastStoneWeight(self, stones):
     
      if len(stones) ==0:
         return 0
      if len(stones) == 1:
         return 1
      while len(stones)>1:
         stones.sort()
         s1,s2=stones[-1],stones[-2]
         if s1==s2:
            stones.pop(-1)
            stones.pop(-1)
         else:
            s1 = abs(s1-s2)
            stones.pop(-1)
            stones[-1] = s1
      if len(stones):
         return stones[-1]
      return 0
ob1 = Solution()
print(ob1.lastStoneWeight([2,7,4,1,6,1]))
