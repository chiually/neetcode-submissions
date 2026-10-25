import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # create heap with freq of each task (heap only contains ready tasks)
        heap = [-freq for freq in Counter(tasks).values()]
        heapq.heapify(heap)
        
        # store tasks that are cannot be done yet
        cooldown = deque()
        time = 0

        while heap or cooldown:
            time += 1
            if heap:
                freq = heapq.heappop(heap) + 1
                if freq:
                    cooldown.append((freq, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])

        return time

            


        