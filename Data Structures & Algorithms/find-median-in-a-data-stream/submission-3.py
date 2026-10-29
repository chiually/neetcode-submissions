import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = [] # right half of list
        self.maxHeap = [] # left half of list
        

    def addNum(self, num: int) -> None:

        if self.minHeap and num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:

            if len(self.minHeap) < len(self.maxHeap):
                val = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -val)
            else:
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -val)
        #print(self.maxHeap, self.minHeap)
        

    def findMedian(self) -> float:

        # if even number of vals
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            # calculate median with root of two heaps
            return (self.minHeap[0] + -self.maxHeap[0]) / 2

        # if odd number of vals
        else:
            # return index 0 at larger heap
            return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
        
        