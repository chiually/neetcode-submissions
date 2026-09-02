class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW, COL = len(grid), len(grid[0])

        def dfs(i, j):

            if i < 0 or j < 0 or i >= ROW or j >= COL or grid[i][j] != '1':
                return

            # mark curr position as visited
            grid[i][j] = '2'

            # explore surrounding area
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        
        count = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count

        

        