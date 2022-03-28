class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr=[]
        for i in range(len(nums)):
            for j in range (i,len(nums)):
                if nums[j]< nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
        for i in range(len(nums)):
            if nums[i]==target:
                arr.append(i)
        return arr
