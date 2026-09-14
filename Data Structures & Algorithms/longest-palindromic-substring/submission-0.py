class Solution:

    def getLengthOfPalindrome(self, s: str, l: int, r: int):

        length = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length = r - l + 1
            l -= 1
            r += 1

        return l + 1, length

    def longestPalindrome(self, s: str) -> str:

        maxLength = 0
        maxStart = 0

        for i in range(len(s)):
            evenStart, evenLength = self.getLengthOfPalindrome(s, i, i + 1)
            oddStart, oddLength = self.getLengthOfPalindrome(s, i, i)
            
            if maxLength < evenLength:
                maxLength, maxStart = evenLength, evenStart
            if maxLength < oddLength:
                maxLength, maxStart = oddLength, oddStart

        return s[maxStart: maxStart + maxLength]

        
        