class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l, r = 0, len(s1) - 1

        permutation = "".join(sorted(s1))
        while r < len(s2):
            p = "".join(sorted(s2[l:r+1]))
            if p == permutation:
                return True
            else:
                l += 1
                r += 1
        return False

        