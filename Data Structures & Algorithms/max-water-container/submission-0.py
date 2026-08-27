class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # store the current max area
        maxArea = 0

        # have pointer at start and end to begin with the maximum width
        # move pointer with the shorter height

        left = 0
        right = len(heights) - 1
        width = right

        while left < right and width > 0:
            area = width * min(heights[left], heights[right])

            if area > maxArea:
                maxArea = area

            width -= 1
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea
        