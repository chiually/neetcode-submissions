class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        # store chars in substring with their last index apperance
        appears = {}

        l = 0
        length = 0

        for r in range(len(s)):

            if s[r] in appears:
                l = max(appears[s[r]] + 1, l)

            appears[s[r]] = r
            length = max(length, r - l + 1)

        return length 


        