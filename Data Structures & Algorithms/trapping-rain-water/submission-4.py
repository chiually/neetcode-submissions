class Solution:
    def trap(self, height: List[int]) -> int:

        # prework
        maxLeft, maxRight = [], []
        res = 0
        for i in range(len(height)):
            maxLeft.append(res)
            res = max(height[i], res)

        res = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight.append(res)
            res = max(height[i], res)
        maxRight.reverse()

        # calculate the area
        area = 0
        for i in range(len(height)):
            area += max(min(maxLeft[i], maxRight[i]) - height[i], 0)

        return area



        