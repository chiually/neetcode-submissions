import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minHeap = []

        for num in nums:

            if k > 0:
                heapq.heappush(minHeap, num)
            elif minHeap[0] < num:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, num)

            k -= 1

        return minHeap[0]
        