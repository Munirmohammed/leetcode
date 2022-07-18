# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        ansL = ans
        output = []
        while(head):
            output.append(head.val)
            head = head.next
        x = len(output)//2
        output = output[x:]
        for i in output:
            ansL.next = ListNode(i)
            ansL = ansL.next
        return ans.next
