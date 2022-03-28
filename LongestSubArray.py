class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
            maxLength = 0
            maxHeap = []
            minHeap = []
            beg = 0
            end = 0
            while (end < len(nums)):
                currEl = nums[end]
                while (len(maxHeap) > 0 and nums[maxHeap[-1]] <= currEl):
                    del maxHeap[-1]
                maxHeap.append(end)
                while (len(minHeap) > 0 and nums[minHeap[-1]] >= currEl):
                    del minHeap[-1]
                minHeap.append(end)
                maxOfSub = nums[maxHeap[0]]
                minOfSub = nums[minHeap[0]]
                if (maxOfSub - minOfSub <= limit):
                    currLength = end - beg + 1
                    if (maxLength < currLength):
                        maxLength = currLength
                else:
                    beg += 1
                    while (len(minHeap) > 0 and minHeap[0] < beg):
                        del minHeap[0]

                    while (len(maxHeap) > 0 and maxHeap[0] < beg):
                        del maxHeap[0]

                end += 1
            return maxLength
