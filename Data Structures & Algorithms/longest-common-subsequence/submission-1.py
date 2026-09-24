class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # use smaller word to find subsequence
        if len(text1) > len(text2):
            bigger_word, word = text1, text2
        else:
            bigger_word, word = text2, text1

        dp = [[0] * (len(bigger_word) + 1) for _ in range(len(word) + 1)]
        
        for i in range(len(word) - 1, -1, -1):
            for j in range(len(bigger_word) - 1, -1, -1):
                if word[i] == bigger_word[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]