class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # do binary search on the speed k

        minSpeed, maxSpeed = 1, max(piles)
        rate = float('inf')
        while minSpeed <= maxSpeed:
            k = (minSpeed + maxSpeed) // 2

            # get total hours at speed k
            total = 0
            for p in piles:
                total += math.ceil(p / k)

            if total <= h:
                rate = min(rate, k)
                maxSpeed = k - 1
            else:
                minSpeed = k + 1

        return rate
        