from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()

        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    x, y = dr + r, dc + c

                    if x >= 0 and y >= 0 and y < cols and x < rows and grid[x][y] == 1:
                        q.append((x, y))
                        grid[x][y] = 2
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1



        