import os

class Day16:
    def __init__(self):
        self.input_content = None
        self.visited = set()
        
    def solve_part1(self):
        self.loadGrid()
        start = (-1, 0, (1, 0))
        return self.traverse(start)
        
        
    def traverse(self, start):
        stack = [start]

        while stack:
            curr = stack.pop()
            x, y, velocity = curr
            vx, vy = velocity
            nx, ny = x + vx, y + vy

            if curr in self.visited:
                continue

            self.visited.add(curr) 

            if ny < 0 or ny >= len(self.grid) or nx < 0 or nx >= len(self.grid[ny]):
                continue  

            position = self.grid[ny][nx]
            
            if position == "-" and vx == 0:
                stack.append((nx, ny, (-1, 0)))
                stack.append((nx, ny, (1, 0)))
                continue

            if position == "|" and vy == 0:
                stack.append((nx, ny, (0, -1)))
                stack.append((nx, ny, (0, 1)))
                continue

            if position == "/":
                stack.append((nx, ny, (-vy, -vx)))
                continue

            if position == "\\":
                stack.append((nx, ny, (vy, vx)))
                continue

            stack.append((nx, ny, velocity))
            
        unique = set()
        for i in self.visited:
            if i[0] < 0 or i[1] < 0:
                continue
            unique.add((i[0], i[1]))
        self.visited = set()
        return len(unique)

    def solve_part2(self):
        res = 0
        
        for y in range(len(self.grid)):
            res = max(res, self.traverse((0, y, (1, 0))))
            
        for x in range(len(self.grid[0])):
            res = max(res, self.traverse((x, 0, (0, 1))))
        
        for y in range(len(self.grid) - 1, -1, -1):
            res = max(res, self.traverse((len(self.grid[0])-1, y, (-1, 0))))
            
        for x in range(len(self.grid[0]) - 1, -1, -1):
            res = max(res, self.traverse((x, len(self.grid)-1, (0, -1))))
                
        return res

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day16", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print()
            for c in line:
                print(c, end="")

solver = Day16()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)

#7183 
