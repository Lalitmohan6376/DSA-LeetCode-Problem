class Solution:
    def numEnclaves(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            count = 1

            count += dfs(row - 1, col)
            count += dfs(row + 1, col)
            count += dfs(row, col - 1)
            count += dfs(row, col + 1)

            return count

        for row in range(rows):
            if grid[row][0] == 1:
                dfs(row, 0)

            if grid[row][cols - 1] == 1:
                dfs(row, cols - 1)

        for col in range(cols):
            if grid[0][col] == 1:
                dfs(0, col)

            if grid[rows - 1][col] == 1:
                dfs(rows - 1, col)

        answer = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    answer += 1

        return answer
