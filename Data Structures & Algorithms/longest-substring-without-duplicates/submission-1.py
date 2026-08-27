class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0

        max_len = 1
        freq = {} # key=char val=last idx

        l = 0 # shrink until dup gone
        r = 0 # expand while no dup
        while r < len(s):
            
            # if left pointer less than last appearance of s[r] --> dup
            if l <= freq.get(s[r], -1):
                l = freq.get(s[r], -1) + 1

            if r - l + 1 > max_len:
                print(l, r)
                max_len = r - l + 1

            # update latest appearance
            freq[s[r]] = r
            r += 1
            print(max_len)

        return max_len


        