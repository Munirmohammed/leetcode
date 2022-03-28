class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums1 = []
        p1, p2 = 0, len(nums)-1
        
        while len(nums1) != len(nums):
            nums1.append(nums[p1])
            p1 += 1
            
            if p1 < p2:
                nums1.append(nums[p2])
                p2 -=1
        return nums1
