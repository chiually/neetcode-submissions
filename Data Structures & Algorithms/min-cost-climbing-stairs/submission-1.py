class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)
        
        # d[i] = the minimum cost to reach each step

        dp = [0] * (len(cost) + 1)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i + 1], cost[i + 2]) + cost[i]

        return min(cost[0], cost[1])