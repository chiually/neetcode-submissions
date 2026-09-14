class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # two subcases of regular liner House Robber problem
        # (1 to n - 1) and (0 to n - 2)
        return max(nums[0], self.getMaxMoney(nums[1:]), self.getMaxMoney(nums[:-1]))
        # need to handle case with only one house since slicing would make arrays empty

    def getMaxMoney(self, nums: List[int]):

        rob1, rob2 = 0, 0 # max money up to i - 1 and i - 2

        for i in range(len(nums)):
            newRob = max(nums[i] + rob2, rob1)
            rob2 = rob1
            rob1 = newRob

        return rob1