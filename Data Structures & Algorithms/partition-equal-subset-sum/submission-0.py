class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums) -1, -1, -1):
            new = set()
            for t in dp:
                new.add(t + nums[i])
                new.add(t)
            dp = new

        return target in dp

        