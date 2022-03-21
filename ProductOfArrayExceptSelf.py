class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            left = 1
            right = 1
            for j in range(0, i):
                left *= nums[j]
            for k in range(i+1, len(nums)):
                right *= nums[k]
            output.append((left*right))
        return output
