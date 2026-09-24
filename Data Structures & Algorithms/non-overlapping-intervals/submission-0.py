class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort by finish time
        intervals.sort(key= lambda x : x[1])

        # if start time of interval less than last VALID finish time, remove interval
        finish = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < finish:
                res += 1
            else:
                finish = intervals[i][1]
        return res



        