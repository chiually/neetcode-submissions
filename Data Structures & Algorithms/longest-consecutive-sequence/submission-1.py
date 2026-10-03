class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # turn list into a set
        nums = set(nums)
        res = 0

        for num in nums:

            # determine if num could be the start of a sequence
            if num - 1 not in nums:
                tmp = 1
                while num + 1 in nums:
                    num += 1
                    tmp += 1
                res = max(res, tmp)

        return res
        