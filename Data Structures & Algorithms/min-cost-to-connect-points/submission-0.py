import heapq
class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # make graph and calc all edges
        n = len(points)
        adj = [[] for _ in range(n)] # number points from 0 to n-1
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((dist, j))
                adj[j].append((dist, i))


        # do prim's algo to find MST
        res = 0
        visit = set()
        minHeap = [(0, 0)] # (cost, point)

        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue

            res += cost
            visit.add(i)
            for neiCost, j in adj[i]:
                if j not in visit:
                    heapq.heappush(minHeap, (neiCost, j))

        return res