class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # make graph
        adj = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # detect cycle in graph using dfs
        visit = [False] * (len(edges) + 1)

        cycle = set()
        cycleStart = -1
        
        def dfs(node, parent):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True # there is cycle

            visit[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                # if there is a cycle:
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    # break out of cycle
                    if node == cycleStart:
                        cycleStart = -1
                    return True                 
            return False

        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []


        
        