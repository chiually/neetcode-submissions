class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        pos = {} # last index of char
        length = 0

        l = 0
        for r in range(len(s)):
            
            # if char already in window
            if s[r] in pos:
                l = max(pos[s[r]] + 1, l)
                
            pos[s[r]] = r
            length = max(length, r - l + 1)

        return length



        