from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # in bfs, only add VALID nodes to the queue
        row, col = len(grid), len(grid[0])
        q = deque()

        # append all thr rotten fruit to the queue
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))

        level = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                # append its neighbours
                for x, y in dirs:
                    rd, cd = r + x, c + y

                    # check the bounds + if fresh
                    if rd >= 0 and cd >= 0 and rd < row and cd < col and grid[rd][cd] == 1:
                        grid[rd][cd] = 2 # mark the fruit
                        q.append((rd, cd))

            level += 1

        # check if any fresh fruit are left in the grid
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1

        return max(0, level - 1)

        
        