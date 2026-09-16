class Solution:
    def validPath(self, n, edges, source, destination):

        graph = {}

        for i in range(n):
            graph[i] = []

        for edge in edges:
            a = edge[0]
            b = edge[1]

            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):

            if node == destination:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)
