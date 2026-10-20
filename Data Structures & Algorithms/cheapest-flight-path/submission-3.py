import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # do dijkstra's algorithm but stop if path is greater than k
        adj = [[] for _ in range(n)]
        for s, d, p in flights:
            adj[s].append((p, d))

        dist = [[float('inf')] * (k + 2) for _ in range(n)] 

        minHeap = [(0, src, -1)]
        dist[src][0] = 0

        # +1 and +2 for indexing purposes
        while len(minHeap):
            cost, airport, stops = heapq.heappop(minHeap)

            if airport == dst:
                return cost
            if stops == k or cost > dist[airport][stops + 1]:
                continue

            for p, d in adj[airport]:
                # if not visited yet
                if dist[d][stops + 2] > p + cost:
                    dist[d][stops + 2] = p + cost
                    heapq.heappush(minHeap, (p + cost, d, stops + 1))

        return -1