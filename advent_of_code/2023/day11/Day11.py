import os

class Day11:
    def __init__(self):
        self.input_content = None
        self.grid = []
    
    def solve(self, part1):
        step = 2 if part1 else 1000000
        self.makeGrid(part1)
        
        galaxies = self.findGalaxies()
        pairs = set()  
        
        for i, galaxy in enumerate(galaxies):
            for other_galaxy in galaxies[i+1:]: 
                if galaxy != other_galaxy:
                    pairs.add(tuple(sorted([galaxy, other_galaxy]))) 
                    
        return sum(self.shortestPath(pair[0], pair[1], step) for pair in pairs)
    
    def shortestPath(self, start, end, step=2):
        x, y = start
        dist = 0
        
        while x != end[0] or y != end[1]:
            if x != end[0]:
                x += 1 if x < end[0] else -1
            else:
                y += 1 if y < end[1] else -1
                
            dist += step-1 if self.grid[y][x] == 'x' else 1
        return dist
    
    def findGalaxies(self):
        galaxies = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == '#':
                    galaxies.append((x, y))
        return galaxies
    
    def makeGrid(self, part1):
        self.grid = []
        
        temp_grid = [list(line) for line in self.input_content.splitlines()]
        height = len(temp_grid)
        width = len(temp_grid[0]) if height > 0 else 0

        for line in temp_grid:
            self.grid.append(list(line))
            if line.count('.') == len(line):
                character = '.' if part1 else 'x'
                self.grid.append(list([character for x in line if x == '.']))
                
        new_grid = []
        for row in self.grid:
            new_row = []
            for x in range(width):
                new_row.append(row[x])
                if all(temp_row[x] == '.' for temp_row in temp_grid):
                    character = '.' if part1 else 'x'
                    new_row.append(character)
            new_grid.append(new_row)

        self.grid = new_grid
    
    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day11", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day11()
solver.loadInputFiles()
part1_result = solver.solve(True)
part2_result = solver.solve(False)

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
