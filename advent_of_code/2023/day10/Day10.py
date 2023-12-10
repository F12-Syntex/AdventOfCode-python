from collections import deque
import os

class Day10:
    def __init__(self):
        self.input_content = None
        
        
    def solve_part1(self):
        # self.printGrid()
        
        visited = set()
        queue = deque([(self.findStartPosition(), 0)]) 
        max_distance = 0
        
        while queue:
            node, distance = queue.popleft()
            if node not in visited:
                visited.add(node)
                max_distance = max(max_distance, distance) 
                
                for neighbour in self.getNeighbours(node):
                    if neighbour not in visited:
                        queue.append((neighbour, distance + 1)) 

        return max_distance
    
    def solve_part2(self):
            pass
    
    
    def getNeighbours(self, node):
        neighbours = []
        
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        
        EAST, WEST, NORTH, SOUTH = 0, 1, 2, 3
        
        row, col = node
        
        if col + 1 < cols and self.grid[row][col][EAST] == 1 and self.grid[row][col + 1][WEST] == 1:
            neighbours.append((row, col + 1))
            
        if col - 1 >= 0 and self.grid[row][col][WEST] == 1 and self.grid[row][col - 1][EAST] == 1:
            neighbours.append((row, col - 1))

        if row + 1 < rows and self.grid[row][col][SOUTH] == 1 and self.grid[row + 1][col][NORTH] == 1:
            neighbours.append((row + 1, col))
            
        if row - 1 >= 0 and self.grid[row][col][NORTH] == 1 and self.grid[row - 1][col][SOUTH] == 1:
            neighbours.append((row - 1, col))

        return neighbours

        
    
    def findStartPosition(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == (1,1,1,1):
                    return (i, j)
        return None

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day10", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = []

        self.offset = [(0, 0, 1, 1), #'|' 
                (1, 1, 0, 0), #'-'
                (1, 0, 1, 0), #'L'
                (0, 1, 1, 0), #'J'
                (0, 1, 0, 1), #'7'
                (1, 0, 0, 1), #'F'
                (0, 0, 0, 0), #'.'
                (1, 1, 1, 1)] #'S'
        self.characters = ['|', '-', 'L', 'J', '7', 'F', '.', 'S']
        
        for line in self.input_content.splitlines():
            row = []
            for character in line:                
                if character in self.characters:
                    row.append(self.offset[self.characters.index(character)])
                else:
                    row.append(character)
            self.grid.append(row)
    
    def characterToOffset(self, character):
        return self.offset[self.characters.index(character)]
    
    def offsetToCharacter(self, offset):
        return self.characters[self.offset.index(offset)]
    
    def printGrid(self):
        print(self.input_content)
        for i in range(len(self.grid)):
            print(self.grid[i])
            
    

solver = Day10()
solver.loadInputFiles()
solver.loadGrid()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
