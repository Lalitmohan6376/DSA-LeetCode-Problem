class Solution:
  def canVisitAllRooms(self, rooms):
    graph = {}
    n = len(rooms)
    
    for i in range(n):
      graph[i] = rooms[i]

    visited = {0}
    front = 0
    q = [0]

    while front < len(q):
      node = q[front]
      front+=1

      for neighbor in  graph[node]:
        if neighbor not in visited:
          visited.add(neighbor)
          q.append(neighbor)
    return len(visited) == n
      

    
