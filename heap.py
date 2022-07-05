class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        larg = i
        left = 2*i+1
        right = 2*i+2
        
        if (left < n and arr[left] > arr[larg]):
            larg = left
        if (right < n and arr[right] > arr[larg]):
            larg = right
        if larg != i:
            arr[i], arr[larg] = arr[larg], arr[i]
            self.heapify(arr, n, larg)
            
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        i = n-2
        while i>=0:
            self.heapify(arr, n, i)
            i -= 1
            
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        i = n-1
        while i>=0:
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,i,0)
            i -= 1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
