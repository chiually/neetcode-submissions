class TimeMap:

    def __init__(self):
        self.mapping = {} # key : [(timestamp, value)] <- sorted by timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:

        vals = self.mapping.get(key, [])
        vals.append((timestamp, value))

        if len(vals) == 1:
            self.mapping[key] = vals
        
    def get(self, key: str, timestamp: int) -> str:
        # recall: timestamps guaranteed to be increasing
        if key not in self.mapping:
            return ""
        timestamps = self.mapping[key]

        # binary search to find rightmost timestamp
        l, r = 0, len(timestamps) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2

            if timestamps[m][0] <= timestamp:
                res = timestamps[m][1]
                l = m + 1
            else:
                r = m - 1

        return res
        
