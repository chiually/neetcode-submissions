class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            w = r - l
        
            # move the smaller height
            if heights[l] < heights[r]:
                max_area = max(max_area, heights[l] * w)
                l += 1
            else:
                max_area = max(max_area, heights[r] * w)
                r -= 1


        return max_area


