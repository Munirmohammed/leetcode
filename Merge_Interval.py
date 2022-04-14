class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: (x[0]))
        ans = []
        ans.append(intervals[0])
        for start_i, end_i in intervals[1:]:
            start_j, end_j = ans[-1]
            if start_i > end_j:
                ans.append([start_i, end_i])
            else:
				# only the end may need to be adapted, 
				# since we sorted the intervals by start, 
				# the new interval is guaranteed to have a start greater or equal to existing one.
                ans[-1][1] = max(end_j, end_i)
        return ans
