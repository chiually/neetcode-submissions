"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        newNodes = {}

        def dfs(node):
            # check if node has been visted or added
            if node in newNodes:
                return newNodes[node]

            copy = Node(node.val)
            # add to mapping
            newNodes[node] = copy
            for neighbour in node.neighbors:
                copy.neighbors.append(dfs(neighbour))
            return copy

        return dfs(node) if node else None