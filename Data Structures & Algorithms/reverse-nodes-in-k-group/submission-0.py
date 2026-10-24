# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # prevGroup is last node in reversed group
        prevGroup = dummy = ListNode(next=head)

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break # if no kth node, don't reverse
            groupNext = kth.next

            # reverse k nodes
            prev, curr = kth.next, prevGroup.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev

                prev = curr
                curr = temp

            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
            
        return dummy.next

    def getKth(self, start, k):

        curr = start
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr
        