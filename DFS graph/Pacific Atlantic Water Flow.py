class Solution:
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row, col, visited):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if (row, col) in visited:
                return

            visited.add((row, col))

            if row > 0 and heights[row - 1][col] >= heights[row][col]:
                dfs(row - 1, col, visited)

            if row < rows - 1 and heights[row + 1][col] >= heights[row][col]:
                dfs(row + 1, col, visited)

            if col > 0 and heights[row][col - 1] >= heights[row][col]:
                dfs(row, col - 1, visited)

            if col < cols - 1 and heights[row][col + 1] >= heights[row][col]:
                dfs(row, col + 1, visited)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result
