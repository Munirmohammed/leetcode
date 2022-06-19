class Solution:

    def findKthLargest(self, nums, k):
        left = 0
        right = len(nums) - 1

        while True:
            index = self.__partition(nums, left, right)
            if index == len(nums) - k:
                return nums[index]
            if index > len(nums) - k:
                right = index - 1
            else:
                left = index + 1

    def __partition(self, nums, left, right):
        
        munir = nums[left]
        k = left
        for index in range(left + 1, right + 1):
            if nums[index] < munir:
                k += 1
                nums[k], nums[index] = nums[index], nums[k]
        nums[left], nums[k] = nums[k], nums[left]
        return k
