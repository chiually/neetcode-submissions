# Doubly Linked List
class Node:
    def __init__(self, key:int , val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map the key to the node

        # create pointers for LRU and MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def markMRU(self, node: Node):
        # if already in list
        if node.prev and node.next:
            n1, n2 = node.prev, node.next

            n1.next = n2
            n2.prev = n1

        old = self.right.prev

        old.next = node
        node.prev = old

        node.next = self.right
        self.right.prev = node

    def removeLRU(self) -> int:
        removed = self.left.next

        old = removed.next

        old.prev = self.left
        self.left.next = old
        
        self.cache.pop(removed.key, None)
        
    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1 

        node = self.cache[key]

        # mark as recently used
        self.markMRU(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # if cache exceeds capacity remove LRU node
        if key not in self.cache and len(self.cache) + 1 > self.capacity:
            print(self.cache)
            self.removeLRU()
        
        # update if already in cache
        if key in self.cache:
            self.cache[key].val = value
        else: 
            # create node
            node = Node(key, value)

            # add to mapping
            self.cache[key] = node

        # mark most recently used
        self.markMRU(self.cache[key])
        
