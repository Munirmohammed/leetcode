class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        
        if count == n:
            itr = head.next
            return itr
        else:
            counter = 0
            itr = head
            while itr:
                if counter == count - n - 1:
                    itr.next = itr.next.next
                counter += 1
                itr = itr.next
        itr = head
        return itr
