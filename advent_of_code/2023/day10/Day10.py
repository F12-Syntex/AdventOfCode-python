from collections import deque
import os

class Day10:
    def __init__(self):
        self.input_content = None
        
        
    def solve_part1(self):
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
                    
        def betterPrint():
            for i in range(len(self.grid)):
                line = ""
                for j in range(len(self.grid[i])):
                    if self.offsetToCharacter(self.grid[i][j]) == '.':
                        line += '\033[91m' + 'I' + '\033[0m'
                    elif self.offsetToCharacter(self.grid[i][j]) == '>':
                        line += '\033[33m' + '>' + '\033[0m'  
                    elif self.offsetToCharacter2(self.grid[i][j]) == '┌':  #
                        line += '\033[95m' + '┌' + '\033[0m'
                    else:
                        line += '\033[95m' + str(self.offsetToCharacter2(self.grid[i][j])) + '\033[0m'

                print(line)



        betterPrint()
                    
        #iterate over the first row and run flood fill
        for i in range(len(self.grid[0])):
            self.floodFill((0, i))
            
        #iterate over the last row and run flood fill
        for i in range(len(self.grid[len(self.grid) - 1])):
            self.floodFill((len(self.grid) - 1, i))
        
        #iterate over the first column and run flood fill
        for i in range(len(self.grid)):
            self.floodFill((i, 0))
        
        #iterate over the last column and run flood fill
        for i in range(len(self.grid)):
            self.floodFill((i, len(self.grid[i]) - 1))
            
        #count all the dots
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.offsetToCharacter(self.grid[i][j]) == '>':
                    count += 1
            
        betterPrint()
        return count
    
    def floodFill(self, node):
        
        char = str(self.offsetToCharacter(self.grid[node[0]][node[1]]))
        if char != ".":
            return
        
        def getNeighbours(node):
            neighbours = []
            
            #get all the nodes, up down left right top right top left bottom right bottom left
            
            if node[0] - 1 >= 0:
                neighbours.append((node[0] - 1, node[1]))
            
            if node[0] + 1 < len(self.grid):
                neighbours.append((node[0] + 1, node[1]))
            
            if node[1] - 1 >= 0:
                neighbours.append((node[0], node[1] - 1))
            
            if node[1] + 1 < len(self.grid[0]):
                neighbours.append((node[0], node[1] + 1))

            return neighbours
        
        queue = deque([node])
        visited = set()
        
        while queue:
            node = queue.popleft()
            # print(node)
            if node not in visited:
                visited.add(node)
                char = "0"
                
                for neighbour in getNeighbours(node):
                    if neighbour not in visited:
                        n_char = str(self.offsetToCharacter(self.grid[neighbour[0]][neighbour[1]]))
                        if n_char == ".":
                            queue.append(neighbour)
                            continue
                        
                        #check if we can pass through this wall
                        node = self.getPassThroughPosition(neighbour)
                        if node:
                            queue.append(node)
                        
                        
        for node in visited:
            self.grid[node[0]][node[1]] = ">"
    
    def inBounds(self, node):
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        
        row, col = node
        
        return row >= 0 and row < rows and col >= 0 and col < cols
    
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
        inputPath = os.path.join(os.getcwd(), "2023", "day10", "test.txt")
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
        self.characters2 = ['│', '─', '└', '┘', '┐', '┌', '.', 'S']
        
        for line in self.input_content.splitlines():
            row = []
            for character in line:                
                if character in self.characters:
                    row.append(self.offset[self.characters.index(character)])
                else:
                    row.append(character)
            self.grid.append(row)
    
    def characterToOffset(self, character):
        if character not in self.characters:
            return str(character)
        return self.offset[self.characters.index(character)]
    
    def offsetToCharacter(self, offset):
        if offset not in self.offset:
            return ">"
        return self.characters[self.offset.index(offset)]
    
    def offsetToCharacter2(self, offset):
        if offset not in self.offset:
            return ">"
        return self.characters2[self.offset.index(offset)]
    
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
