import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # max heap of size k
        closest_points = []

        for x, y in points:

            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(closest_points, (-dist, (x, y)))

            if len(closest_points) > k:
                heapq.heappop(closest_points)

        return [x[1] for x in closest_points]

        