# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head
        prev = None

        reorder = []
        while curr.next:
            prev = curr
            curr = curr.next

            reorder.append(prev)
        # curr is last element in list
        node = head
        while node and node.next:
            if reorder:
                prev = reorder.pop()
                prev.next = None

            temp = node.next
            node.next = curr
            curr.next = temp

            curr = prev
            node = temp


