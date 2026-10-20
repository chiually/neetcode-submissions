class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1 = self.getRob(nums[:len(nums) - 1])
        rob2 = self.getRob(nums[1:])

        return max(rob1, rob2, nums[0])

    def getRob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return 0 if not nums else nums[0]

        # dp[i] = max amount you can rob at house i

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[len(nums) - 1]

        