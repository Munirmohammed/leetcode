class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        leftPointer, rightPointer =0,0
        res,total =0,0
        
        while rightPointer < len(nums):
            total += nums[rightPointer]
            
            while nums[rightPointer] * (rightPointer - leftPointer +1) > total + k:
                total -= nums[leftPointer]
                leftPointer +=1
                
            
            res = max(rightPointer -leftPointer +1,res)
            
            rightPointer +=1
        
        return res
