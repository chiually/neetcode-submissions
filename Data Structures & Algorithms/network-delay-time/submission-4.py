import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # make the graph
        adj = [[] for _ in range(n + 1)]    
        for u, v, t in times:
            adj[u].append((v, t))

        # run dijktras algo on the graph

        heap = [(0, k)] # total time, node
        visit = set()

        time = 0

        while heap:
            for _ in range(len(heap)):
                total, u = heapq.heappop(heap)
                if u in visit:
                    continue
                visit.add(u)
                time = total

                for nei, t in adj[u]:
                    heapq.heappush(heap, (t + total, nei))
        
        return time if len(visit) == n else -1
