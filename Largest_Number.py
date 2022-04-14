import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sorted_by(a, b):
            if a+b > b+a:
                return 1
            elif a+b < b+a:
                return -1
            else:
                return 0
        cmp = functools.cmp_to_key(sorted_by)
        return "".join(sorted([str(x) for x in nums], key=cmp, reverse=True)).lstrip('0') or '0'
