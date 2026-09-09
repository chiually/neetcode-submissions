class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        count = 0

        # create the graph
        mapping = {i : [] for i in range(n)}
        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u)

        visited = set()
        def dfs(node):
            
            if node in visited:
                return

            visited.add(node)
            for nei in mapping[node]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count
        