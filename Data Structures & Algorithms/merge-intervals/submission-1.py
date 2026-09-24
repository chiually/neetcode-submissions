class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x : x[1])

        finish = intervals[0][1] # last valid finish time
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            curr = intervals[i]

            if finish >= curr[0]:
                old = res.pop()
                while len(res) > 0 and res[-1][0] > curr[0]:
                    old = res.pop()

                res.append([min(old[0], curr[0]), curr[1]])
            else:
                res.append(curr)

            finish = curr[1]

        return res


        