class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list) # key : (timestamp, value)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((timestamp, value))

        # since set is increasing order, timestamps are ascending
        

    def get(self, key: str, timestamp: int) -> str:
        # assume the mapping is not empty (set called prev)

        # get list of (timestamp, values) associated with the keys
        values = self.mapping[key]
        l, r = 0, len(values) - 1

        res = ""
        while l <= r:
            m = (l + r) // 2
            t, val = values[m]

            if t <= timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1

        return res

        
