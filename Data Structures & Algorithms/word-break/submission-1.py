class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # base case: always true for empty string

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break # don't need to check rest of words

        return dp[0]
