class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProd = minProd = 1

        res = nums[0]
        for num in nums:
            prod = maxProd * num # 0 means we need to restart running product

            maxProd = max(num * minProd, prod, num)
            minProd = min(num * minProd, prod, num)

            res = max(res, maxProd) # handles 0s

        return res




