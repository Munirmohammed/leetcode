class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = 0
        rem = 0
        sumlist = ListNode()
        node = ListNode()
        sumlist = node
        while l1 != None or l2 != None:
            numl1 = l1.val if l1 != None else 0
            numl2 = l2.val if l2 != None else 0
            result = numl1 + numl2
            if (result+rem) > 9:
                node.val = (result+rem) % 10
                rem = (result+rem) // 10
                
            else:
                node.val = (result+rem)
                rem = 0
            
            if l1 != None:
                l1 = l1.next
                
            if l2 != None:
                l2 = l2.next
                
            if l1 != None or l2 != None:
                node.next = ListNode()
                node = node.next
            elif rem != 0:
                node.next = ListNode()
                node = node.next
                node.val = rem
                
            
        return sumlist
