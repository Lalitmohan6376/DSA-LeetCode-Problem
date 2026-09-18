class Solution:
    def dfs(self, adj):
        visited = set()
        ans = []

        def dfs(vertex):
            visited.add(vertex)
            ans.append(vertex)

            for neighbor in adj[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        return ans
