class Solution:
    def shortestPath(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        q = [(0, 0, 0, 0)]
        front = 0
        visited = {(0, 0, 0)}

        while front < len(q):
            row, col, used, steps = q[front]
            front += 1

            if row == m - 1 and col == n - 1:
                return steps

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < m and 0 <= new_col < n:
                    new_used = used + grid[new_row][new_col]

                    if new_used <= k:
                        state = (new_row, new_col, new_used)

                        if state not in visited:
                            visited.add(state)
                            q.append((new_row, new_col, new_used, steps + 1))

        return -1
