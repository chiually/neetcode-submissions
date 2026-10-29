class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {} # ith day, whether you can buy or sell that day

        def dfs(i, buy):

            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]

            cooldown = dfs(i + 1, buy)
            if buy:
                # sell the next day or wait to buy
                dp[(i, buy)] = max(dfs(i + 1, not buy) - prices[i], cooldown)
                return dp[(i, buy)]
            else:
                # need to wait at least a day to buy
                dp[(i, buy)] = max(dfs(i + 2, not buy) + prices[i], cooldown)
                return dp[(i, buy)]

        return dfs(0, True)