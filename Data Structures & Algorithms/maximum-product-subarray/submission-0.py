class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curMax = curMin = 1

        for num in nums:
            prod = num * curMax

            curMax = max(num, prod, num * curMin)
            curMin = min(num, prod, num * curMin)

            res = max(res, curMax)

        return res
