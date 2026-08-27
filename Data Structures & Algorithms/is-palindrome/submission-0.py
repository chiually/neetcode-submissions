class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean input: put s in all lowercase and only keep alphanumeric chars
        cleaned = "".join(char.lower() for char in s if char.isalnum())

        # have two pointers for start and end of string
        start = 0
        end = len(cleaned) - 1

        while start <= end:
            # if pointers do not match return false
            if cleaned[start] != cleaned[end]:
                return False

            start += 1
            end -= 1

        return True
        