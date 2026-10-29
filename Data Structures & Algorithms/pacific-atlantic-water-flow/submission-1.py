class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
        atl, pac = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(i, j, visit, prevHeight):

            if (i, j) in visit or i >= ROWS or i < 0 or j >= COLS or j < 0 or prevHeight > heights[i][j]:
                return

            visit.add((i,j))

            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])

        # search everything reachable from the atlantic/pacific ocean
        for i in range(ROWS):
            dfs(i, COLS - 1, atl, -1)
            dfs(i, 0, pac, -1)

        for j in range(COLS):
            dfs(ROWS - 1, j, atl, -1)
            dfs(0, j, pac, -1)

        # if in both atl and pac sets append to res
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i, j])

        return res


        