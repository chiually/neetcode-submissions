class Solution:
    def numDecodings(self, s: str) -> int:

        # go through it backwards and keep how many ways you can decode up to that point

        if not s:
            return 0

        # dp[i] = how many ways to decode the string[i:]
        dp = [0] * (len(s))
        dp[-1] = 1 if s[-1] != "0" else 0
        dp.append(1) # base case: empty string has one valid decoding

        for i in range(len(s) - 2, -1, -1):

            if s[i] == "0":
                continue
            else:
                dp[i] = dp[i + 1]

            if s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456":
                dp[i] += dp[i + 2]
        
        return dp[0]

            



        