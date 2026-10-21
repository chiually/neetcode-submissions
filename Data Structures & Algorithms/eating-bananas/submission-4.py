class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # sort the list
        piles.sort()

        # range of speeds
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2

            # get total hours to eat all bananas at speed m
            total = 0
            for p in piles:
                total += math.ceil(p / m)

            # if total hours < h
            if total <= h:
                # search the left half of speeds
                res = m
                r = m - 1
            # otherwise couldn't eat in time 
            else:
                # search the right half of speeds (need to increase k)
                l = m + 1

        return res
        