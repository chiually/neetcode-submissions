class Solution:
    def numDecodings(self, s: str) -> int:
        
        # dp[i] is the number of ways to decode the substring s[i:]
        dp = {len(s) : 1} # base case: empty string has one valid decoding

        # n - 1 to 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0 # since invalid
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]

        return dp[0]