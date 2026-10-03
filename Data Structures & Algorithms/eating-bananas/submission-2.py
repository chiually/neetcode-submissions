class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles) # min speed, max speed
        res = r

        while l <= r:
            speed = (r + l) // 2

            # total hours using this speed
            totalHours = 0
            for p in piles:
                totalHours += math.ceil(float(p) / speed)

            if totalHours <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1

        return res