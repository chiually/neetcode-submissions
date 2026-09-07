class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # dfs with cycle detection

        # trees have exactly n - 1 edges
        if len(edges) > n - 1:
            return False

        # build graph --> undirected
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visit = set()

        # since undirected graph, we need to pass parent to prevent counting the pair edge as a cycle
        def dfs(i, par):

            if i in visit:
                return False

            visit.add(i)
            for nei in adjList[i]:
                if nei == par:
                    continue
                if not dfs(nei, i):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n # make sure graph is connected


        