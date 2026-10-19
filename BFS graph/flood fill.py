class Solution:
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])

        original = image[sr][sc]

        if original == color:
            return image

        queue = [(sr, sc)]
        front = 0

        image[sr][sc] = color

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while front < len(queue):
            r, c = queue[front]
            front += 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == original:
                        image[nr][nc] = color
                        queue.append((nr, nc))

        return image


solution = Solution()

image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

print(solution.floodFill(image, sr, sc, color))
