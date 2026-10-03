"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        new = Node(0)
        dummy = Node(0, new)
        nodes = {}

        curr = head
        while curr:

            # if the node was already created
            if curr in nodes:
                new = nodes[curr]
            else:
                new.val = curr.val
                nodes[curr] = new

            if curr.next in nodes:
                new.next = nodes[curr.next]
            elif curr.next:
                new.next = Node(curr.next.val)
                nodes[curr.next] = new.next

            if curr.random in nodes:
                new.random = nodes[curr.random]
            elif curr.random:
                new.random = Node(curr.random.val)
                nodes[curr.random] = new.random

            new = Node(0)
            curr = curr.next

        return dummy.next if head else None
        