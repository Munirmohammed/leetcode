class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        y = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    y +=1
        return y
