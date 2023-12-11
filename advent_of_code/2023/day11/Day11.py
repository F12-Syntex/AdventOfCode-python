from collections import deque
import os
import heapq

class Day11:
    def __init__(self):
        self.input_content = None
        self.grid = []

    def solve_part1(self):
        self.makeGrid()
        galaxies = self.findGalaxies()
        pairs = set()  
        
        for i, galaxy in enumerate(galaxies):
            for other_galaxy in galaxies[i+1:]: 
                if galaxy != other_galaxy:
                    pairs.add(tuple(sorted([galaxy, other_galaxy]))) 
                    
        galaxies = sorted(galaxies)
        pairs = sorted(pairs)
        
        sum = 0
        for pair in pairs:
            p1, p2 = pair
            sum += self.shortestPath(p1, p2)
        
        return sum
        
    def shortestPath(self, start, end):
        dx, dy = abs(end[0] - start[0]), abs(end[1] - start[1])
        return dx + dy
    
    def shortestPathP2(self, start, end):
        x, y = start
        dist = 0

        while x != end[0] or y != end[1]:
            if x < end[0]:
                x += 1
            elif x > end[0]:
                x -= 1
            elif y < end[1]:
                y += 1
            elif y > end[1]:
                y -= 1
            dist += 1000000-1 if self.grid[y][x] == 'x' else 1

        return dist

    def solve_part2(self):
        self.makeGridP2()
        galaxies = self.findGalaxies()
        pairs = set()  
        
        for i, galaxy in enumerate(galaxies):
            for other_galaxy in galaxies[i+1:]: 
                if galaxy != other_galaxy:
                    pairs.add(tuple(sorted([galaxy, other_galaxy]))) 
                    
        galaxies = sorted(galaxies)
        pairs = sorted(pairs)
        
        sum = 0
        for pair in pairs:
            p1, p2 = pair
            sum += self.shortestPathP2(p1, p2)
        
        return sum
    
    def findGalaxies(self):
        galaxies = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == '#':
                    galaxies.append((x, y))
        return galaxies
    
    def findGalaxyPairs(self, galaxy):
        galaxies = self.findGalaxies()
        x1, y1 = galaxy

        pairs = [((x2, y2), (x1, y1)) for x2, y2 in galaxies if x2 != x1 or y2 != y1]
        return pairs
    
    def makeGridP2(self):
        
        self.grid = []
        
        temp_grid = [list(line) for line in self.input_content.splitlines()]
        height = len(temp_grid)
        width = len(temp_grid[0]) if height > 0 else 0

        for line in temp_grid:
            self.grid.append(list(line))
            if line.count('.') == len(line):
                line = ['x' for x in line if x == '.']
                self.grid.append(list(line))
        new_grid = []
        for row in self.grid:
            new_row = []
            for x in range(width):
                new_row.append(row[x])
                if all(temp_row[x] == '.' for temp_row in temp_grid):
                    new_row.append('x')
            new_grid.append(new_row)

        self.grid = new_grid
    
    def makeGrid(self):
        
        self.grid = []
        
        temp_grid = [list(line) for line in self.input_content.splitlines()]
        height = len(temp_grid)
        width = len(temp_grid[0]) if height > 0 else 0

        for line in temp_grid:
            self.grid.append(list(line))
            if line.count('.') == len(line):
                self.grid.append(list(line))

        new_grid = []
        for row in self.grid:
            new_row = []
            for x in range(width):
                new_row.append(row[x])
                if all(temp_row[x] == '.' for temp_row in temp_grid):
                    new_row.append('.')
            new_grid.append(new_row)

        self.grid = new_grid
                    
    def print(self):
        for line in self.grid:
            print(line)

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day11", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day11()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
