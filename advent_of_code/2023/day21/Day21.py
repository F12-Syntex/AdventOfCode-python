from collections import deque
import os
import time
from AOCInputGrabber import AOCInputGrabber

class Day21:
    def __init__(self):
        self.input_content = None
        self.DAY = 21
        self.YEAR = 2023
        self.aoc_utils = AOCInputGrabber(self.YEAR, self.DAY)

    def solve_part1(self):
        self.loadGrid()

        start = self.find_start()

        steps = 6
        queue = [start]
        for _ in range(steps):
            queue = self.step(queue)

        return len(queue)

    def solve_part2(self):
        grid = self.input_content.splitlines()

        sr, sc = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

        assert len(grid) == len(grid[0])

        size = len(grid)
        steps = 26501365

        assert sr == sc == size // 2
        assert steps % size == size // 2

        def fill(sr, sc, ss):
            ans = set()
            seen = {(sr, sc)}
            q = deque([(sr, sc, ss)])

            while q:
                r, c, s = q.popleft()

                if s % 2 == 0:
                    ans.add((r, c))
                if s == 0:
                    continue

                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr, nc) in seen:
                        continue
                    seen.add((nr, nc))
                    q.append((nr, nc, s - 1))
            
            return len(ans)

        grid_width = steps // size - 1

        odd = (grid_width // 2 * 2 + 1) ** 2
        even = ((grid_width + 1) // 2 * 2) ** 2

        odd_points = fill(sr, sc, size * 2 + 1)
        even_points = fill(sr, sc, size * 2)

        corner_t = fill(size - 1, sc, size - 1)
        corner_r = fill(sr, 0, size - 1)
        corner_b = fill(0, sc, size - 1)
        corner_l = fill(sr, size - 1, size - 1)

        small_tr = fill(size - 1, 0, size // 2 - 1)
        small_tl = fill(size - 1, size - 1, size // 2 - 1)
        small_br = fill(0, 0, size // 2 - 1)
        small_bl = fill(0, size - 1, size // 2 - 1)

        large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
        large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
        large_br = fill(0, 0, size * 3 // 2 - 1)
        large_bl = fill(0, size - 1, size * 3 // 2 - 1)

        return  odd * odd_points + even * even_points + corner_t + corner_r + corner_b + corner_l + (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) + grid_width * (large_tr + large_tl + large_br + large_bl)
        
    
    def step(self, positions):
        visited = set()
        for position in positions:
            x, y = position
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                
                ny = ny % len(self.grid)
                nx = nx % len(self.grid[ny])

                if self.is_valid(nx, ny):
                    visited.add((nx, ny))
        
        for x, y in visited:
            self.grid[y][x] = "O"
        for x, y in positions:
            self.grid[y][x] = "."
        return visited


    def is_valid(self, x, y):
        return self.grid[y][x] == "."

    def find_start(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == "S":
                    return (x, y)

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().rstrip()

        inputFile = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        if not os.path.exists(inputFile):
            content = self.aoc_utils.grab_input().rstrip()
            with open(inputFile, "w") as f:
                f.write(content)
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)

solver = Day21()
solver.loadInputFiles()

start_time_part1 = time.time()
part1_result = solver.solve_part1()
end_time_part1 = time.time()
print("Solution to Part 1:", part1_result, "completed in", round((end_time_part1 - start_time_part1) * 1000), "ms")

start_time_part2 = time.time()
part2_result = solver.solve_part2()
end_time_part2 = time.time()
print("Solution to Part 2:", part2_result, "completed in", round((end_time_part2 - start_time_part2) * 1000), "ms")
