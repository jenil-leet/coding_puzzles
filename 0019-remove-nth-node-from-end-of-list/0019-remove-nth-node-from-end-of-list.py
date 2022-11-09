# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        lenlist = 0
        t = head
        while(t!=None):
            t = t.next
            lenlist += 1
        if(1 == lenlist):
            return None
        
        idx_to_remove = lenlist - n
        if(0 == idx_to_remove):
            return head.next
        
        t = head
        while( idx_to_remove > 1 ):
            t = t.next
            idx_to_remove-=1
        #now remove
        t.next = t.next.next
        return(head)