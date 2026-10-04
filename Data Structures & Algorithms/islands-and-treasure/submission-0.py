class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = (2**31) - 1
        print(INF)
        ROWS, COLS = len(grid), len(grid[0])

        # shortest path to treasure chest == BFS!
        q = collections.deque()

        # add all treasure chest locations to the queue
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        length = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row < ROWS and col < COLS and row >= 0 and col >= 0 and grid[row][col] == INF:
                        grid[row][col] = length
                        q.append((row, col))

            length += 1

                
        
        
        