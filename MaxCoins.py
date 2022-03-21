class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        temp = []
        new = []
        while True:
            temp.append(piles.pop(0))
            temp.append(piles.pop())
            temp.insert(1, piles.pop())
            new.append(temp)
            temp = []
            if len(piles) == 0:
                break
        for i in new:
            piles.append(i[1])
        s = 0
        for i in piles:
            s += i
        return s
        """
        :type piles: List[int]
        :rtype: int
        """
