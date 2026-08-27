class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        
        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        return countS == countT
        