class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, index):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if (row, col) in visited:
                return False

            if board[row][col] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            visited.add((row, col))

            if dfs(row - 1, col, index + 1):
                return True

            if dfs(row + 1, col, index + 1):
                return True

            if dfs(row, col - 1, index + 1):
                return True

            if dfs(row, col + 1, index + 1):
                return True

            visited.remove((row, col))

            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
