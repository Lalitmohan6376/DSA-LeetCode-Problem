class Solution:
    def findMaxFish(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        max_fish = 0
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if grid[row][col] == 0:
                return 0

            fish = grid[row][col]
            grid[row][col] = 0

            fish += dfs(row - 1, col)
            fish += dfs(row + 1, col)
            fish += dfs(row, col - 1)
            fish += dfs(row, col + 1)

            return fish

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    fish = dfs(row,col)
                    max_fish = max(max_fish,fish)
        return max_fish
