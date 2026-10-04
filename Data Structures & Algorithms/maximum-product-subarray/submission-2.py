class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProd, minProd = 1, 1
        res = nums[0]

        for num in nums:
            prod = maxProd * num

            maxProd = max(num, prod, num * minProd)
            minProd = min(num, prod, num * minProd)

            res = max(res, maxProd)

        return res