class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = collections.deque()
        
        # determine number of fresh fruit and queue rotting fruit
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                # queue neighbours
                for dr, dc in dirs:
                    row, col = r + dr, c + dc

                    # check bounds and if fresh
                    if row >= 0 and col >= 0 and row < ROW and col < COL and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1

        
        