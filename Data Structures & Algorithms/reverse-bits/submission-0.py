class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):

            # extract ith bit of n
            bit = (n >> i) & 1 # recall 1 is 0001 in binary

            # shift bit to (31 - i)th position and add to res
            res += (bit << (31 - i))

        return res
        