import os
import time
from heapq import heappush, heappop

class Day17:
    def __init__(self):
        self.input_content = None

    def solve(self, MAX_STEPS, STEPS_REQUIRED_TO_TURN, MIN_STEPS_WITHOUT_TURN_TO_STOP):
        self.loadGrid()

        visited = set()
        pq = [(0, 0, 0, 0, 0, 0)]  # heat loss, x, y, direction_x, direction_y, steps

        while pq:
            heat_loss, x, y, dx, dy, steps = heappop(pq)

            if y == len(self.grid) - 1 and x == len(self.grid[0]) - 1 and steps >= MIN_STEPS_WITHOUT_TURN_TO_STOP:
                return heat_loss 

            if (x, y, dx, dy, steps) in visited:
                continue

            visited.add((x, y, dx, dy, steps))

            if steps < MAX_STEPS and (dx, dy) != (0, 0):
                nx, ny = x + dx, y + dy
                if self.in_bounds(nx, ny):
                    heappush(pq, (heat_loss + self.grid[ny][nx], nx, ny, dx, dy, steps + 1))

            if steps >= STEPS_REQUIRED_TO_TURN or (dx, dy) == (0, 0):
                for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (ndx, ndy) != (dx, dy) and (ndx, ndy) != (-dx, -dy):
                        nx, ny = ndx + x, ndy + y
                        if self.in_bounds(nx, ny):
                            heappush(pq, (heat_loss + self.grid[ny][nx], nx, ny, ndx, ndy, 1))

        return -1

    def in_bounds(self, x, y):
        return y >= 0 and y < len(self.grid[0]) and x >= 0 and x < len(self.grid)
    
    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day17", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[int(c) for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)

solver = Day17()
solver.loadInputFiles()

start_time_part1 = time.time()
part1_result = solver.solve(3, 0, 0)
end_time_part1 = time.time()
print("Solution to Part 1:", part1_result, "completed in", round((end_time_part1 - start_time_part1) * 1000), "ms")

start_time_part2 = time.time()
part2_result = solver.solve(10, 4, 4)
end_time_part2 = time.time()
print("Solution to Part 2:", part2_result, "completed in", round((end_time_part2 - start_time_part2) * 1000), "ms")

