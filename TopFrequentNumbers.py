class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = []
        u = []
        for i in nums:
            if [1,i] not in x:
                x.append([1,i])
                a = nums.index(i)
                u.append(i)
        for i in u:
            nums.remove(i)
        print(u)
        print(x)
        for j in nums:
            for l in range(len(x)):
                if x[l][1] == j:
                    x[l][0] +=1
        print(x)
        x = Solution.mergeSort(x)
        print(x)
        
        y = []
        for n in range(1,k+1):
            z= x[-n][1]
            print(z)
            y.append(z)
        return (y)
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            Solution.mergeSort(L)
            Solution.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][0] < R[j][0]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr
