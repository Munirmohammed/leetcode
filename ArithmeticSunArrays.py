class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        answer=[]
        for i in range(len(l)):
            if r[i]==len(nums)-1:
                temp = nums[l[i]:]
            else:
                temp=nums[l[i]:(r[i]+1)]
            temp.sort()
            difference=temp[1]-temp[0]
            j=0
            tempBool=True
            while j<len(temp)-1:
                if temp[j+1]-temp[j] != difference:
                    tempBool=False
                j+=1
            answer.append(tempBool)
        return answer
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
