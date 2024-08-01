# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy=ListNode(0)
        even_dummy=ListNode(0)
        odd_current=odd_dummy
        even_current=even_dummy
        current=head
        index=1
        while current:
            if index%2!=0:
                odd_current.next=current
                odd_current=odd_current.next
            else:
                even_current.next=current
                even_current=even_current.next
            current=current.next
            index+=1
        even_current.next=None
        odd_current.next=even_dummy.next
        return odd_dummy.next
