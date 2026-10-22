class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        minimum = float("inf")
        while l <= r:
            m = (l + r) // 2

            minimum = min(nums[m], minimum)

            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

        return minimum


# [6,1,2,3,4,5]

# [3,4,5,6,1,2]

        