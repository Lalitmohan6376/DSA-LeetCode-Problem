class Solution:
    def canVisitAllRooms(self, rooms):
        graph = {}
        
        for i in range(len(rooms)):
            graph[i] = rooms[i]
        
        visited = set()
        
        def dfs(room):
            visited.add(room)
            
            for next_room in graph[room]:

                if next_room not in visited:
                    dfs(next_room)

        dfs(0)

        return len(visited) == len(rooms)



#optimize solution

class Solution:
    def canVisitAllRooms(self, rooms):

        visited = set()

        def dfs(room):
            visited.add(room)

            for next_room in rooms[room]:
                if next_room not in visited:
                    dfs(next_room)

        dfs(0)

        return len(visited) == len(rooms)
