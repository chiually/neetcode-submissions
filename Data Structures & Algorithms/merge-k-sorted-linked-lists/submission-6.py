# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class NodeWrapper:

    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, NodeWrapper(l))

        curr = dummy
        while heap:
            # pop the min node
            node = heapq.heappop(heap)

            # add node to final list
            curr.next = ListNode(node.node.val)
            curr = curr.next

            # push back to heap if not None
            if node.node.next:
                heapq.heappush(heap, NodeWrapper(node.node.next))

        return dummy.next