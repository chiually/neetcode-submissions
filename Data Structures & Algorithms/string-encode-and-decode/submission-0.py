class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            n = len(s)
            res.append(str(n) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        while i < len(s):
            # get number of letters in string
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length
            res.append(s[i: j])

            i = j

        return res

