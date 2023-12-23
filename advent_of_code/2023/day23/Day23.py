import collections
import os
import time
from typing import Deque

from AOCInputGrabber import AOCInputGrabber


class Day23:
    def __init__(self):
        self.input_content = None
        self.DAY = 23
        self.YEAR = 2023
        self.aoc_utils = AOCInputGrabber(self.YEAR, self.DAY)
    
    def solve(self, part1):
        graph = self.simplifyEdges(part1)
        visited = set()
        return self.bruteForceSearch(self.start, graph, visited)
    
    def bruteForceSearch(self, location, edges, visited):
        if location == self.end:
            return 0
        
        distance = -float("inf")

        visited.add(location)
        for point in edges[location]:
            if point not in visited:
                distance = max(distance, self.bruteForceSearch(point, edges, visited) + edges[location][point])
        visited.remove(location)
        return distance


    def getNeighbors(self, location, part1):
        x, y = location
        neighbors = []

        if not self.is_valid_move(x, y):
            return neighbors

        if self.grid[y][x] in "><^v" and part1:
            offset = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}[self.grid[y][x]]
            nx, ny = x + offset[0], y + offset[1]
            if self.is_valid_move(nx, ny):
                neighbors.append((nx, ny))
            return neighbors

        for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + offset[0], y + offset[1]
            if self.is_valid_move(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
    
    def is_valid_move(self, x, y):
        return 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid) and self.grid[y][x] != "#"

    def simplifyEdges(self, part1):
        edges = {}
        hotspots = self.identifyHotSpots(part1)

        for hx, hy in hotspots:
            queue = [(0, hx, hy)]
            visited = [(hx, hy)]

            while queue:
                neighbors, x, y = queue.pop()
                if neighbors > 0 and (x, y) in hotspots:
                    if (hx, hy) not in edges:
                        edges[(hx, hy)] = {}
                    edges[(hx, hy)][(x, y)] = neighbors
                    continue
                    
                for nx, ny in self.getNeighbors((x, y), part1):
                    if (nx, ny) in visited:
                        continue
                    queue.append((neighbors+1, nx, ny))
                    visited.append((nx, ny))
        return edges


    def identifyHotSpots(self, part1):
        queue = [self.start]
        visited = []
        res = {self.start, self.end}
        while queue:
            curr = queue.pop()
            if curr in visited:
                continue
            neighbors = self.getNeighbors(curr, part1)
            if len(neighbors) > 2:
                res.add(curr)
            visited.append(curr)
            queue.extend(neighbors)
        return res

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().rstrip()

        inputFile = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        if not os.path.exists(inputFile):
            content = self.aoc_utils.grab_input().rstrip()
            with open(inputFile, "w") as f:
                f.write(content)

        self.loadGrid()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        self.start = (self.grid[0].index("."), 0)
        self.end = (self.grid[-1].index("."), len(self.grid)-1)
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print()
            for ch in line:
                print(ch, end=" ")
        print()

solver = Day23()
solver.loadInputFiles()

start_time_part1 = time.time()
part1_result = solver.solve(True)
end_time_part1 = time.time()
print("Solution to Part 1:", part1_result, "completed in", round((end_time_part1 - start_time_part1) * 1000), "ms")

start_time_part2 = time.time()
part2_result = solver.solve(False)
end_time_part2 = time.time()
print("Solution to Part 2:", part2_result, "completed in", round((end_time_part2 - start_time_part2) * 1000), "ms")
