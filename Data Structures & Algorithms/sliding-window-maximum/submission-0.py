import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maxHeap = [] # store (num, idx)
        res = []

        for r in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[r], r))
            if r < k - 1:
                continue

            l = r - k + 1
            val, idx = heapq.heappop(maxHeap)
            while idx < l:
                val, idx = heapq.heappop(maxHeap)

            res.append(-val)
            if idx > l:
                heapq.heappush(maxHeap, (val, idx))

        return res
        