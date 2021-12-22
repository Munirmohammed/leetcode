class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        A = [0] * 102        
        for mun in nums:
            A[mun + 1] += 1            
        for i in range(1, 102):
            A[i] += A[i - 1]            
        result = []        
        for mun in nums:
            result.append(A[mun])
        
        return result
