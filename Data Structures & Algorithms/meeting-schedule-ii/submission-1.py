"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()

        s = e = count = 0
        res = 0
        while s < len(starts) and e < len(ends):

            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        # return number of overlapping intervals
        return res

        