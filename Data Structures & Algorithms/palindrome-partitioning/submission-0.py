class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        new = []

        def dfs(i, j):

            if i >= len(s) or j >= len(s):
                return
            
            # partition the string if palindrome
            if self.isPalindrome(s, i,  j):

                new.append(s[i: j + 1])
                for k in range(j + 1, len(s)):
                    dfs(j + 1, k)

                if j == len(s) - 1:
                    res.append(new.copy())
                new.pop()

            return


        # check every substring starting at index 0
        for j in range(len(s)):
            dfs(0, j)

        return res

    def isPalindrome(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True
        