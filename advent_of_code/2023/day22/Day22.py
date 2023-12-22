import os
import time
from AOCInputGrabber import AOCInputGrabber
import string

class Day22:
    def __init__(self):
        self.input_content = None
        self.DAY = 22
        self.YEAR = 2023
        self.aoc_utils = AOCInputGrabber(self.YEAR, self.DAY)

    def solve_part1(self):
        # Define the grid and bricks
        grid = []
        
        
        bricks = []
        labels = []

        index = 0
        for line in self.input_content.splitlines():
            start, end = line.split("~")
            start = list(map(int, start.split(",")))
            end = list(map(int, end.split(",")))
            bricks.append((start, end))
            labels.append(string.ascii_uppercase[index])
            index += 1

        # Determine the maximum dimensions for the grid
        max_x = max(max(start[0], end[0]) for start, end in bricks)
        max_y = max(max(start[1], end[1]) for start, end in bricks)
        max_z = max(max(start[2], end[2]) for start, end in bricks)

        # Create the 3D grid to represent the settled position of the bricks
        grid = [[[None for _ in range(max_z + 1)] for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        # Iterate through each brick and update the settled position based on the support from other bricks
        for (x1, y1, z1), (x2, y2, z2) in bricks:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    for z in range(min(z1, z2), max(z1, z2) + 1):
                        grid[y][x][z] = (x1, y1, z1, x2, y2, z2)

        # Determine the number of bricks that are not supporting other bricks
        disintegrated = 0

        # supportingBricks = {}

        # #remove all bricks that would not change the position of any other bricks
        # for y in range(len(bricks)):
        #     brick1 = bricks[y]
        #     supporting = []
        #     for x in range(len(bricks)):
        #         brick2 = bricks[x]

        #         #if the z value of brick1 is more than the z value of brick2, then skip
        #         if brick1[0][2] >= brick2[0][2]:
        #             continue

        #         supporting.append(brick2)

        #     builder = ""
        #     supportingBricks[labels[y]] = supporting
        #     for brick in supporting:
        #         builder += labels[bricks.index(brick)] + " "
        #     print(labels[y], "is supporting:", builder)
        
        return disintegrated

    #is brick1 supporting brick2?
    def is_supporting(self, brick1, brick2):

        brick1_start, brick1_end = brick1
        brick2_start, brick2_end = brick2

        b1x1, b1y1, _ = brick1_start
        b1x2, b1y2, _ = brick1_end

        b2x1, b2y1, _ = brick2_start
        b2x2, b2y2, _ = brick2_end

        if brick1 == brick2:
            return True
        
        for x in range(b1x1, b1x2):
            for y in range(b1y1, b1y2):
                if (x >= b2x1 and x <= b2x2) or (y >= b2y1 and y <= b2y2):
                    return True
        
        return False


    def solve_part2(self):
        return 0
    
    def printGrid(self, grid):
        for z in range(len(grid[0][0])):
            print("\nz =", z)
            for y in range(len(grid)):
                line = ""
                for x in range(len(grid[0])):
                    if grid[y][x][z] is None:
                        line += "."
                    else:
                        line += str(grid[y][x][z])
                print(line)

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().rstrip()

        inputFile = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        if not os.path.exists(inputFile):
            content = self.aoc_utils.grab_input().rstrip()
            with open(inputFile, "w") as f:
                f.write(content)

solver = Day22()
solver.loadInputFiles()

start_time_part1 = time.time()
part1_result = solver.solve_part1()
end_time_part1 = time.time()
print("Solution to Part 1:", part1_result, "completed in", round((end_time_part1 - start_time_part1) * 1000), "ms")

start_time_part2 = time.time()
part2_result = solver.solve_part2()
end_time_part2 = time.time()
print("Solution to Part 2:", part2_result, "completed in", round((end_time_part2 - start_time_part2) * 1000), "ms")
