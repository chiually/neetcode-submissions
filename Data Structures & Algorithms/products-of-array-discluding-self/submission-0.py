class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        n = len(nums)
        multiplier = 1

        for num in nums:
            res.append(multiplier)
            multiplier *= num

        multiplier = 1
        i = len(nums) - 1
        for num in reversed(nums):
            res[i] *= multiplier

            multiplier *= num
            i -= 1

        return res


        