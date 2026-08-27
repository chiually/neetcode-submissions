class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        l = 0 # start of window

        # store freq of each char in window
        freqs = {}
        max_freq = 0

        for r in range(len(s)):

            # get length of window and most freq char
            length = r - l + 1
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            max_freq = max(max_freq, freqs[s[r]])

            # if diff greater than k, restart window
            if length - max_freq > k:
                freqs[s[l]] -= 1 # decrease freq
                l += 1

            res = max(res, r - l + 1) # works since size of window is valid
            
        return res

        