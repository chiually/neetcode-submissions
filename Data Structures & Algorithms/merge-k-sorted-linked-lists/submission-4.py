# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeLists(self, l1, l2):

        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 or l2

        return dummy.next  

    def divide(self, lists, l, r):

        if l > r:
            return None
        if l == r:
            return lists[l]

        mid = l + (r - l) // 2

        l1 = self.divide(lists, l, mid)
        l2 = self.divide(lists, mid + 1, r)

        return self.mergeLists(l1, l2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        l, r = 0, len(lists) - 1
        return self.divide(lists, l, r) if lists else None

        