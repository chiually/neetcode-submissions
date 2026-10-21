class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq = Counter(s1)
        k = len(s1)

        # map of chars in the window
        curr = {}

        l = 0
        for r in range(len(s2)):
            curr[s2[r]] = curr.get(s2[r], 0) + 1
            if r >= k:
                # remove from curr
                if curr[s2[l]] == 1:
                    curr.pop(s2[l])
                else:
                    curr[s2[l]] -= 1

                l += 1

            if curr == freq:
                return True

        return False
        