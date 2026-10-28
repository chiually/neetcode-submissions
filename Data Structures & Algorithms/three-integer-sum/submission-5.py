class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        prev = None
        for i, num in enumerate(nums):
            if prev == num:
                continue 

            target = -num

            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = nums[l] + nums[r]

                if currSum == target:
                    res.append([num, nums[l], nums[r]])

                    r -= 1
                    l += 1

                    while l < len(nums) and nums[l] == nums[l -1]:
                        l += 1

                elif currSum < target:
                    l += 1
                else:
                    r -= 1


            prev = num

        return res
        