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
        grid = self.input_content.splitlines()

        for r, row in enumerate(grid):
            for c, ch in enumerate(row):
                if ch == "S":
                    sr = r
                    sc = c
                    break
            else:
                continue
            break

        loop = {(sr, sc)}
        q = deque([(sr, sc)])

        maybe_s = {"|", "-", "J", "L", "7", "F"}

        while q:
            r, c = q.popleft()
            ch = grid[r][c]

            if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in loop:
                loop.add((r - 1, c))
                q.append((r - 1, c))
                if ch == "S":
                    maybe_s &= {"|", "J", "L"}
                
            if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in loop:
                loop.add((r + 1, c))
                q.append((r + 1, c))
                if ch == "S":
                    maybe_s &= {"|", "7", "F"}

            if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in loop:
                loop.add((r, c - 1))
                q.append((r, c - 1))
                if ch == "S":
                    maybe_s &= {"-", "J", "7"}

            if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in loop:
                loop.add((r, c + 1))
                q.append((r, c + 1))
                if ch == "S":
                    maybe_s &= {"-", "L", "F"}

        assert len(maybe_s) == 1
        (S,) = maybe_s

        grid = [row.replace("S", S) for row in grid]
        grid = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)) for r, row in enumerate(grid)]

        outside = set()

        for r, row in enumerate(grid):
            within = False
            up = None
            for c, ch in enumerate(row):
                if ch == "|":
                    assert up is None
                    within = not within
                elif ch == "-":
                    assert up is not None
                elif ch in "LF":
                    assert up is None
                    up = ch == "L"
                elif ch in "7J":
                    assert up is not None
                    if ch != ("J" if up else "7"):
                        within = not within
                    up = None
                elif ch == ".":
                    pass
                else:
                    raise RuntimeError(f"unexpected character (horizontal): {ch}")
                if not within:
                    outside.add((r, c))
                    
        print(len(grid) * len(grid[0]) - len(outside | loop))

    def identifyPipe(self, sx, sy):
        intersection = set(self.offset.keys())
        
        around = [
            (sx, sy - 1), #left
            (sx, sy + 1), #right
            (sx - 1, sy), #up
            (sx + 1, sy)  #down
        ]    
        
        for point in around:
            dx, dy = point[0] - sx, point[1] - sy
            
            if not self.valid_move(point[0], point[1]):
                continue
            
            pipes = self.findPipesThatCanConnect(self.grid[point[1]][point[0]], (dx, dy))
            
            if len(pipes) == 0:
                continue
            
            intersection = intersection.intersection(pipes) 
        
        intersection.remove('S')
    
        return intersection.pop()

    #suppose pipe is in a point 0, 0, which pipes would be able to connect to it at direction (dx, dy)?
    def findPipesThatCanConnect(self, pipe, direction):        
        LEFT, RIGHT, UP, DOWN = (0, 1, 2, 3)
        
        pipes = set()
        
        #go through all possible pipes and see if they can connect to the pipe we are looking at
        for cpipe in self.offset.keys():
            if direction == (-1, 0):
                #pipe to find is on the left of the pipe, so we need to make sure the pipe can go left, 
                #and the pipe we are looking at can go right
                if self.offset[pipe][LEFT] == 1 and self.offset[cpipe][RIGHT] == 1:
                    pipes.add(cpipe)
            if direction == (1, 0):
                #pipe to find is on the right of the pipe, so we need to make sure the pipe can go right, 
                #and the pipe we are looking at can go left
                if self.offset[pipe][RIGHT] == 1 and self.offset[cpipe][LEFT] == 1:
                    pipes.add(cpipe)
            if direction == (0, -1):
                #pipe to find is on the top of the pipe, so we need to make sure the pipe can go up, 
                #and the pipe we are looking at can go down
                if self.offset[pipe][DOWN] == 1 and self.offset[cpipe][UP] == 1:
                    pipes.add(cpipe)
            if direction == (0, 1):
                #pipe to find is on the bottom of the pipe, so we need to make sure the pipe can go down, 
                #and the pipe we are looking at can go up
                if self.offset[pipe][UP] == 1 and self.offset[cpipe][DOWN] == 1:
                    pipes.add(cpipe)
        
        return pipes
        
    
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
        inputPath = os.path.join(os.getcwd(), "2023", "day10", "input.txt")
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
