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
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        min_rooms, curr_rooms = 0, 0
        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                curr_rooms += 1
                s += 1
            else:
                curr_rooms -= 1
                e += 1
            min_rooms = max(min_rooms, curr_rooms)

        return min_rooms



        