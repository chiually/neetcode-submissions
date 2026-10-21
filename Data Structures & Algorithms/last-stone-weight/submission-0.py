import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # use a max heap
        heap = [-w for w in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # pop the two heaviest stones
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, x - y)

        return -heap[0] if len(heap) == 1 else 0


        