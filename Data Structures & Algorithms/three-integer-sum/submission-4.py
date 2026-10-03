class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        nums.sort()
        for i in range(n):
            target = -nums[i]
            l, r = i + 1, n - 1

            # skip duplicate
            if i > 0 and -target == nums[i - 1]:
                continue

            while l < r:
                currSum = nums[l] + nums[r]

                if currSum == target:
                    res.append([-target, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip any duplicate values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                elif currSum < target:
                    l += 1
                else:
                    r -= 1

        return res



