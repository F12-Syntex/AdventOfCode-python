from collections import deque
import os

class Day10:
    def __init__(self):
        self.input_content = None
        
        #E W N S
        #L R U D
        self.offset = { '|' : (0, 0, 1, 1), #'|' 
                        '-' : (1, 1, 0, 0), #'-'
                        'L' : (1, 0, 1, 0), #'L'
                        'J' : (0, 1, 1, 0), #'J'
                        '7' : (0, 1, 0, 1), #'7'
                        'F' : (1, 0, 0, 1), #'F'
                        '.' : (0, 0, 0, 0), #'.'
                        'S' : (1, 1, 1, 1)} #'S'
    
    def solve_part1(self):

        sy, sx = self.getStart()
        
        visited = {(sy, sx)}
        queue = deque([(sy, sx)])

        while queue:
            x, y = queue.popleft()
            
            for point in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if self.canExplore(x, y, point) and (x + point[0], y + point[1]) not in visited:
                        queue.append((x + point[0], y + point[1]))
                        visited.add((x + point[0], y + point[1]))

        return len(visited) // 2
    
        
    def solve_part2(self):
        sy, sx = self.getStart()

        # The two pipes that the animal can go to 
        points = ((sy+y, sx+x) for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)] if self.valid_move(sy+x, sx+y) and self.canExplore(sy, sx, (x, y)))
        intersection = set(self.offset.keys())

        print(intersection)
            

        return 0
    
    def canExplore(self, sx, sy, direction):
        ex = sx + direction[0]
        ey = sy + direction[1]
        
        if not self.valid_move(ex, ey):
            return False
        
        sc = self.grid[sx][sy]
        ec = self.grid[ex][ey]
        
        mx, my = (0, 0)

        if direction == (-1, 0):
            mx, my = (2, 3)
        if direction == (1, 0):
            mx, my = (3, 2) 
        if direction == (0, -1):
            mx, my = (1, 0)
        if direction == (0, 1):
            mx, my = (0, 1)
        
        return self.offset[sc][mx] == 1 and self.offset[ec][my] == 1 and self.offset[ec] != 'S'
    
    def valid_move(self, x, y):
        return 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid)
    
    def getStart(self):
        for y, line in enumerate(self.grid):
            for x, ch, in enumerate(line):
                if ch == "S":
                    return (y, x)

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day10", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
            
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)

solver = Day10()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)
