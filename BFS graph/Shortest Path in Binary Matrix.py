class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = [[0, 0, 1]]
        front = 0
        grid[0][0] = 1

        while front < len(q):
            row, col, count = q[front]
            front += 1

            if row == n-1 and col == n-1:
                return count

            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                        grid[r][c] = 1
                        q.append([r, c, count+1])

        return -1
