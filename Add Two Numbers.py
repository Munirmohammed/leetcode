# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        tem1,tem2 = l1,l2
        while tem1 != None:
            n = tem1.val + tem2.val + carry
            carry = 0
            
            if n >= 10:
                carry = 1
                n = n%10
            
            tem2.val = n
            tem1 = tem1.next
            if tem2.next == None:
                if tem1 == None and carry == 1:
                    tem2.next = ListNode()
                    tem2 = tem2.next
                else:
                    tem2.next = tem1
                    tem2 = tem2.next
                break
            tem2 = tem2.next
            
        while tem2 != None:
            n = tem2.val + carry
            carry = 0
            
            if n >= 10:
                carry = 1
                n = n%10
            
            tem2.val = n
            if tem2.next == None and carry == 1:
                tem2.next = ListNode(val=1)
                carry = 0
                break
                
            tem2 = tem2.next
            
                
        return l2
