class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
       
        cursum = 0
        prefixsums = {}
        for i in range(len(nums)):
            prefixsums[i] = cursum
            cursum +=  nums[i]
        total = cursum
        
        for i in range(len(nums)):
            if prefixsums[i] == total - prefixsums[i] - nums[i]:
                return i
        return -1
