class Solution(object):
    def minimumBuckets(self, street):
        result = 0
        street = list(street)
        for i, c in enumerate(street):
            if c != 'H' or (i and street[i-1] == 'B'):
                continue
            if i+1 < len(street) and street[i+1] == '.':
                street[i+1] = 'B'
                result += 1
            elif i and street[i-1] == '.':
                street[i-1] = 'B'
                result += 1
            else:
                return -1
        return result
