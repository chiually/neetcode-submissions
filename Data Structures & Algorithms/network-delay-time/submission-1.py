class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # make graph, storing (node, time)
        adj = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj[u].append((v, t))

        min_times = [float('inf')] * (n + 1)
        min_times[0] = 0

        path = set()
        def dfs(node, t):

            if t >= min_times[node]:
                return

            min_times[node] = min(t, min_times[node])

            for nei, time in adj[node]:
                dfs(nei, t + time)


        dfs(k, 0)
        # if inf still in min_times, node is unreachable == not all nodes can get signal
        time = max(min_times)
        return time if time != float('inf') else -1