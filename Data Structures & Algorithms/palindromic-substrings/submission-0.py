class Solution:

    def countPalindrome(self, s: str, l: int, r: int):
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count

    def countSubstrings(self, s: str) -> int:

        count = 0

        # for each possible center
        for i in range(len(s)):

            # check for even palindrome
            count += self.countPalindrome(s, i, i + 1)

            # check for odd palindrome
            count += self.countPalindrome(s, i, i)


        return count
        