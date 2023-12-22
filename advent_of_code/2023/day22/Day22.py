import os
import string
import time

from AOCInputGrabber import AOCInputGrabber


class Day22:
    def __init__(self):
        self.input_content = None
        self.DAY = 22
        self.YEAR = 2023
        self.aoc_utils = AOCInputGrabber(self.YEAR, self.DAY)

    def solve_part1(self):

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

        max_x = max(max(start[0], end[0]) for start, end in bricks)
        max_y = max(max(start[1], end[1]) for start, end in bricks)
        max_z = max(max(start[2], end[2]) for start, end in bricks)

        grid = [[[None for _ in range(max_z + 1)] for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        for (x1, y1, z1), (x2, y2, z2) in bricks:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    for z in range(min(z1, z2), max(z1, z2) + 1):
                        grid[y][x][z] = (x1, y1, z1, x2, y2, z2)

        supporting = {}

        for supporting_brick_index in range(len(bricks)):
            supporting_brick = bricks[supporting_brick_index]

            supporting_bricks = []
            for brick_index in range(len(bricks)):
                brick = bricks[brick_index]

                if not self.is_supporting(supporting_brick, brick):
                    continue

                # print(labels[supporting_brick_index], "supporting", labels[brick_index], "?")
                supporting_bricks.append(brick_index)

            supporting[supporting_brick_index] = supporting_bricks

        supportedBy = {}
        for k, v in supporting.items():

            supported_by = []
            for k2, v2 in supporting.items():
                if k in v2:
                    supported_by.append(k2)
            supportedBy[k] = supported_by

        
        # print("Supporting:", supportedBy)
        a = {}
        for k, v in supportedBy.items():
            # print(labels[k], "supported by", [labels[x] for x in v])
            for value in v:
                if value not in a:
                    a[value] = []
                a[value].append(set(list([labels[x] for x in v])))

        snum = 0

        for k, v in a.items():
            # print(labels[k], "supported by", v)
            for j in v:
                if len(j) == 1:
                    snum += 1

        return len(bricks) - snum

    #is brick1 supporting brick2?
    def is_supporting(self, brick1, brick2):

        brick1_start, brick1_end = brick1
        brick2_start, brick2_end = brick2

        b1x1, b1y1, b1z1 = brick1_start
        b1x2, b1y2, b1z2 = brick1_end

        b2x1, b2y1, b2z1 = brick2_start
        b2x2, b2y2, b2z2 = brick2_end

        b1zmax = max(b1z1, b1z2)
        b2zmin = min(b2z1, b2z2) 

        if brick1 == brick2:
            return False
        
        for x in range(b1x1, b1x2+1):
            for y in range(b1y1, b1y2+1):
                if (x >= b2x1 and x <= b2x2) and (y >= b2y1 and y <= b2y2):
                    if b1zmax < b2zmin:
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
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
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
