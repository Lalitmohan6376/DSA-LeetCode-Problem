class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":

                    queue = [(r, c)]
                    grid[r][c] = "0"  
                    front = 0
                    
                    while front < len(queue):
                        curr_r, curr_c = queue[front]
                        front += 1
                        
                        for dr, dc in directions:
                            new_r = curr_r + dr
                            new_c = curr_c + dc
                            if 0 <= new_r < rows and 0 <= new_c < cols:
                                if grid[new_r][new_c] == "1":
                                    queue.append((new_r, new_c))
                                    
                                    grid[new_r][new_c] = "0"
                                    
        return island
