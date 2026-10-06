class Solution:
    def countSubIslands(self, grid1, grid2):
        rows = len(grid2)
        cols = len(grid2[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return True

            if grid2[row][col] == 0:
                return True

            grid2[row][col] = 0

            valid = True

            if grid1[row][col] == 0:
                valid = False

            if not dfs(row - 1, col):
                valid = False

            if not dfs(row + 1, col):
                valid = False

            if not dfs(row, col - 1):
                valid = False

            if not dfs(row, col + 1):
                valid = False

            return valid

        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    if dfs(row, col):
                        count += 1

        return count
