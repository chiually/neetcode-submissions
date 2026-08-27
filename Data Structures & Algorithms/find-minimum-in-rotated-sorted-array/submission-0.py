class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1 

        while l < r: # found min when l == r
            mid = (l + r) // 2

            # if array not rotated
            if nums[l] < nums[r]:
                return nums[l]
                
            else:

                if nums[mid] < nums[l] and nums[mid] < nums[mid - 1]:
                    return nums[mid]
                # if mid rotated
                elif nums[mid] >= nums[l]:
                    l = mid + 1
                # if mid not rotated
                else:
                    r = mid - 1

        return nums[r]