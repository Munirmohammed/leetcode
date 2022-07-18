from collections import Counter

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        start = head
        nums = []
        while(start):
            nums.append(start.val)
            start = start.next
        z = Counter(nums)
        
        holder = ListNode()
        start = holder
        
        for i in z:
            if z[i] == 1:
                start.next = ListNode(i)
                start = start.next
        return holder.next
