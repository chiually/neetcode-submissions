# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        curr = head
        node = dummy # (n + 1)th node

        while curr:
            if n <= 0:
                node = node.next

            curr = curr.next
            n -= 1

        node.next = node.next.next

        return dummy.next

        
