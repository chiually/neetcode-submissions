# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # two pointer n nodes apart

        dummy = ListNode(0, head) # makes deletion of head easier
        left = dummy
        right = head

        k = 0
        while k < n:
            right = right.next
            k += 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next