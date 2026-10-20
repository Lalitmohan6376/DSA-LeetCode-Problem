
class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        queue = []
        front = 0

        distance = [[-1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    distance[r][c] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while front < len(queue):
            curr_r, curr_c = queue[front]
            front += 1

            for dr, dc in directions:
                new_r = curr_r + dr
                new_c = curr_c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if distance[new_r][new_c] == -1:
                        distance[new_r][new_c] = distance[curr_r][curr_c] + 1
                        queue.append((new_r, new_c))

        return distance
