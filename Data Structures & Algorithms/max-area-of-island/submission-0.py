class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])

        def dfs(i, j):
            area = 0

            if i < 0 or j < 0 or i >= ROW or j >= COL:
                return area

            if grid[i][j] == 1:
                # mark as vistied
                grid[i][j] = 2
                area += 1

                area += dfs(i + 1, j)
                area += dfs(i, j + 1)
                area += dfs(i - 1, j)
                area += dfs(i, j - 1)

            return area

        areas = []
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    areas.append(dfs(i, j))

        return max(areas) if areas else 0

        