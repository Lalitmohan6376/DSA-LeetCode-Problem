
class Solution:
    def validPath(self, n, edges, source, destination):
        graph = {}

        for i in range(n):
            graph[i] = []

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = {source}
        front = 0
        queue = [source]

        while front < len(queue):
            node = queue[front]
            front += 1

            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False
