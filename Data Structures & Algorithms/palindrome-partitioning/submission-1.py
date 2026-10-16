class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        new = []

        def dfs(i, j):

            if j >= len(s):
                
                # if on last char
                if j == i:
                    res.append(new.copy())
                return
            
            # partition the string if palindrome
            if self.isPalindrome(s, i,  j):
                new.append(s[i: j + 1])
                # start new partition
                dfs(j + 1, j + 1)
                new.pop()

            # check every substring starting at index i
            dfs(i, j + 1)

        dfs(0, 0)

        return res

    def isPalindrome(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True
        