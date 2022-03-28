class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        ans = 0

        for i in range(1, len(nums)):
            curr = nums[i]

            if pre >= curr:

                ans += pre - curr + 1
                curr = pre + 1

            pre = curr

        return ans
