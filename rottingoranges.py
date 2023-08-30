#994. Rotting Oranges

class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return 0
        fresh_coords = set()
        rotten_coords = set()
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_coords.add((i, j))
                elif grid[i][j] == 2:
                    rotten_coords.add((i, j))
                    
        return self.recursive(fresh_coords, rotten_coords, rows, cols)
        
    
    def recursive(self, fresh_coords, rotten_coords, rows, cols):
        if not fresh_coords:
            return 0
        if not rotten_coords:
            return -1
        newly_rotten = set()
        
        # start finding newly rotten oranges
        for fresh in fresh_coords:
            for neighbor in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = fresh[0] + neighbor[0]
                y = fresh[1] + neighbor[1]
                if x >= 0 and x < rows and y >= 0 and y < cols and (x, y) in rotten_coords:
                    newly_rotten.add(fresh)
                            
        if not newly_rotten:
            return -1
        else:
            for coords in newly_rotten:
                fresh_coords.remove(coords)
                rotten_coords.add(coords)
                
            temp = self.recursive(fresh_coords, rotten_coords, rows, cols)
            if temp == -1:
                return -1
            else:
                return 1 + temp
