import os

class Day14:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        grid = [[c for c in line] for line in self.input_content.split("\n")]
        
        grid = self.flipGravity(grid)
            
        return self.score(grid)
    
    def solve_part2(self):
        grid = [[c for c in line] for line in self.input_content.split("\n")]
        
        res = {}

        target = 1000000000
        curr = 0
        
        while curr<target:
            curr += 1
            grid = self.cycle(grid)   
            
            serialisable_grid = tuple(tuple(row) for row in grid)
            if serialisable_grid in res:
                cycle_length = curr - res[serialisable_grid]
                future_discoveries = (target-curr)//cycle_length
                curr += future_discoveries * cycle_length 
                 
            res[serialisable_grid] = curr
        return self.score(grid)

    def cycle(self, grid):
        for _ in range(4):
            grid = self.flipGravity(grid)
            grid = self.turn(grid)
        return grid

    def turn(self, G):
        rows, cols = len(G), len(G[0])
        grid = [['' for _ in range(rows)] for _ in range(cols)]
        
        for r in range(rows):
            for c in range(cols):
                grid[c][rows-1-r] = G[r][c]
        return grid
    
    def flipGravity(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 'O':
                    self.flipGravityAt(grid, x, y)
        return grid
    
    def flipGravityAt(self, grid, x, y):
            ny = y
            while ny > 0 and grid[ny-1][x] == '.':
                ny -= 1
            grid[y][x] = '.'
            grid[ny][x] = 'O'
    
    def score(self, grid):
        sum = 0
        for y in range(len(grid)):
            level = len(grid) - y
            sum += grid[y].count('O') * level
        return sum
    
    
    def print_grid(self, grid):
        print()
        for row in grid:
            print("".join(row))

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day14", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day14()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)