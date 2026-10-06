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

            # Current cell grid1 में भी 1 होना चाहिए
            if grid1[row][col] == 1:
                valid = True
            else:
                valid = False

            # चारों directions
            if dfs(row - 1, col) == False:
                valid = False

            if dfs(row + 1, col) == False:
                valid = False

            if dfs(row, col - 1) == False:
                valid = False

            if dfs(row, col + 1) == False:
                valid = False

            return valid

        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    if dfs(row, col) == True:
                        count += 1

        return count
