class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT) # unique chars in t

        l = 0
        res, len_res = [-1, -1], float('inf')

        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1

            # works since will only increment if equal to count in countT
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:

                if (r - l + 1) < len_res:
                    res = [l, r]
                    len_res = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if len_res != float('inf') else ""



        