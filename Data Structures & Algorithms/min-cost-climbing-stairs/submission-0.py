class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = cost.copy()
        n = len(cost)

        for i in range(2, n):
            dp[i] += min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])
        