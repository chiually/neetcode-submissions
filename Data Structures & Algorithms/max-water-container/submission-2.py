class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            width = r - l
            h1, h2 = heights[l], heights[r]

            area = width * min(h1, h2)
            res = max(res, area)

            if h1 < h2:
                l += 1
            else:
                r -= 1

        return res

        