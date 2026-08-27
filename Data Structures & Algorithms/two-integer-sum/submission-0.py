class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {} # key=complement value=idx

        for i in range(len(nums)):
            num = nums[i]

            if num in complement:
                return [complement[num], i]

            complement[target - num] = i

        return []

        