class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i][j] = length of longest increasing subsequence from s[i:] where j is index of last element in seq

        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # iterate i from n - 1 to 0
        for i in range(n - 1, -1, -1):

            # iterate j from i - 1 to -1
            for j in range(i - 1, -2, -1):
                LIS = dp[i + 1][j + 1]

                if j == -1 or nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[i + 1][i + 1])

                dp[i][j + 1] = LIS

        return dp[0][0]