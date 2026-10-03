class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        multiplier = 1
        
        for num in nums:
            res.append(multiplier)
            multiplier *= num
                
        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= multiplier
            multiplier *= nums[i]
            
        return res
        