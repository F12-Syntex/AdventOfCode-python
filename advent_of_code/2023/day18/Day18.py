import os

class Day18:
    def __init__(self):
        self.input_content = None

    def solve_part12(self):
        self.grid = []
        x, y = 0, 0 

        for line in self.input_content.splitlines():
            direction = line.split()[0]
            dist = int(line.split()[1])

            ex, ey = x, y

            if direction == 'L':
                ex -= dist
            if direction == 'R':
                ex += dist
            if direction == 'U':
                ey -= dist
            if direction == 'D':
                ey += dist

            self.grid.append(((x, y), (ex, ey)))
            x, y = ex, ey

        # the key is the y axis, and the value is a tuple containing the min and max x value for that y axis
        mapping = {}
        for start, end in self.grid:
            sx, sy = start
            ex, ey = end

            for i in range(min(sy, ey), max(sy, ey) + 1):
                if i not in mapping:
                    mapping[i] = (min(sx, ex), max(sx, ex))
                else:
                    cur_min, cur_max = mapping[i]
                    mapping[i] = (min(cur_min, min(sx, ex)), max(cur_max, max(sx, ex)))

        for key in mapping:
            print(key, mapping[key])

        res = 0
        for key in mapping:
            minx, maxx = mapping[key]
            res += abs(maxx - minx) + 1

        return res
    
    def solve_part1(self):
        # self.grid = [['.' for _ in range(-200, 200)] for _ in range(-200, 200)]
        self.grid = [['.' for _ in range(10)] for _ in range(10)]
        x, y = 0, 0 

        for line in self.input_content.splitlines():
            direction = line.split()[0]
            dist = int(line.split()[1])

            print(direction, dist)

            ex, ey = 0, 0

            if direction == 'L':
                ex = x - dist
                while x > ex:
                    self.grid[y][x] = '#'
                    x -= 1

            if direction == 'R':
                ex = x + dist
                while x < ex:
                    self.grid[y][x] = '#'
                    x += 1

            if direction == 'U':
                ey = y - dist
                while y > ey:
                    self.grid[y][x] = '#'
                    y -= 1

            if direction == 'D':
                ey = y + dist
                while y < ey:
                    self.grid[y][x] = '#'
                    y += 1

        self.grid[y][x] = '#'
            
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != '#':
                    self.grid[y][x] = 'X'
                else:
                    break

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])-1, -1, -1):
                if self.grid[y][x] != '#':
                    self.grid[y][x] = 'X'
                else:
                    break

                
        # Add top to bottom
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid)):
                if self.grid[y][x] != '#':
                    self.grid[y][x] = 'X'
                else:
                    break

        # Add bottom to top
        for x in range(len(self.grid[0])):
            for y in range(len(self.grid)-1, -1, -1):
                if self.grid[y][x] != '#':
                    self.grid[y][x] = 'X'
                else:
                    break
        
        c = 0
        for line in self.grid:
            for ch in line:
                if ch == '.' or ch == '#':
                    c += 1
            
        for line in self.grid:
            print(line)

        return c
    
    def solve_part2(self):
        return 0

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day18", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)


#25681

solver = Day18()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)
