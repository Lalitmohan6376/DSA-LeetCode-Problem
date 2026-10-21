class Solution:
    def isBipartite(self, graph):
      n = len(graph)

      group = [-1] * n

      for i in range(n):
        if group[i] == -1:
          queue = [i]
          front = 0
          group[i] = 0

          while front < len(queue):
            node = queue[front]
            front+=1

            for neighbour in graph[node]:
              if group[neighbour] == -1:
                group[neighbour] = 1-group[node]
                queue.append(neighbour)
              elif group[neighbour] == group[node]:
                return False
      return True
