# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode(0,head)
        current=dummy
        arr=[]
        while current:
            arr.append(current.val)
            current=current.next
        print(arr[:0:-1])
        if arr[1::]==arr[:0:-1]:
            return True
        return False
