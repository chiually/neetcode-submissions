class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        xor = n

        for i in range(n):
            # anything xor itself is 0
            # anyting xor 0 is itself
            xor ^= i ^ nums[i]
        return xor