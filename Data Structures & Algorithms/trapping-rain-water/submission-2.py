class Solution:

    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(height[l], maxL)

                res += max(maxL - height[l], 0)

            else:
                r -= 1
                maxR = max(height[r], maxR)
                
                res += max(maxR - height[r], 0)

        return res
