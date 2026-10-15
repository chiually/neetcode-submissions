# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        curr = dummy
        carry = 0
        while l1 and l2:

            total = l1.val + l2.val

            val = (total + carry) % 10
            curr.next = ListNode(val)

            carry = 1 if total + carry >= 10 else 0

            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        if (not l1 and l2) or (l1 and not l2):
            l = l1 if l1 else l2

            while l:
                val = (l.val + carry) % 10

                curr.next = ListNode(val)
                carry = 1 if l.val + carry >= 10 else 0

                l = l.next
                curr = curr.next

        if carry == 1:
            curr.next = ListNode(1)

        return dummy.next

        