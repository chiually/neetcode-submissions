class Solution:
    def isPalindrome(self, s: str) -> bool:

        # clean the string
        s = "".join(char for char in s if char.isalnum()).lower()

        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else: 
                return False

        return True
        