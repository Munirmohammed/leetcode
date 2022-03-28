class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      
        last = slow = fast = head
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
       
        last.next = None
       
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        oriNode = head
        midNode = prev
        while oriNode and midNode:
            temp = oriNode.next
            temp2 = midNode.next
            oriNode.next = midNode
            midNode.next = temp
            last = midNode
            oriNode = temp
            midNode = temp2
            
        if midNode:
            last.next = midNode
