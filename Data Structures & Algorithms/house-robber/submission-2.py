class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if not nums: 
            return 0
        if n == 1:
            return nums[0]

        # dp[i] the max amount of money you can rob from ith house (does not need to inculde the ith house)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]
        