from collections import deque
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

        self.X_START = 0
        self.Y_START = 1
        self.Z_START = 2
        self.X_END = 3
        self.Y_END = 4
        self.Z_END = 5

    def solve_part1(self):


        bricks = self.parseInput()
        self.simulate_falling(bricks)
        
        #find all the brick to support and support to relationships
        keys, values = self.findSupports(bricks)

        #for every brick, count all bricks that support 2 or more bricks (which means removing them would not cause a chain reaction)
        return sum(1 for i in range(len(bricks)) if all(len(values[j]) >= 2 for j in keys[i]))

    def solve_part2(self):
        bricks = self.parseInput()
        self.simulate_falling(bricks)
        
        keys, values = self.findSupports(bricks)

        res = 0

        for i in range(len(bricks)):
            queue= deque()

            #Add all the bricks that will cause a chain reaction if disintegrated to a queue
            for j in keys[i]:
                if len(values[j]) == 1:
                    queue.append(j)

            #bfs we start with the brick we are trying to disintegrate
            falling = set(queue)
            falling.add(i)
            
            #for every brick in the queue, remove all the falling bricks that are supported by it
            #then check if everything in falling is in the values for that brick
            #add the length of the collision and add it to the queue
            while queue:
                j = queue.popleft()
                for k in keys[j]:
                    if k in falling:
                        continue
                    if values[k] <= falling:
                        queue.append(k)
                        falling.add(k)
                    
            
            res += len(falling) - 1

        return res

    def simulate_falling(self, bricks):
        for index, brick in enumerate(bricks):
            max_z = 1
            for check in bricks[:index]:
                if self.intersects(brick, check):
                    max_z = max(max_z, check[self.Z_END] + 1)
            brick[self.Z_END] -= brick[self.Z_START] - max_z
            brick[self.Z_START] = max_z
            
        bricks.sort(key=lambda brick: brick[2])

    def findSupports(self, bricks):
        keys = {i: set() for i in range(len(bricks))}
        values = {i: set() for i in range(len(bricks))}

        for j, top_brick in enumerate(bricks):
            for i, bottom_brick in enumerate(bricks[:j]):
                if self.intersects(bottom_brick, top_brick) and top_brick[self.Z_START] == bottom_brick[self.Z_END] + 1:
                    keys[i].add(j)
                    values[j].add(i)
        return keys, values

    def intersects(self, brick1, brick2):
        return (max(brick1[self.X_START], brick2[self.X_START]) <= min(brick1[self.X_END], brick2[self.X_END])) and (max(brick1[self.Y_START], brick2[self.Y_START]) <= min(brick1[self.Y_END], brick2[self.Y_END]))

    def parseInput(self):
        bricks = []
        for line in self.input_content.splitlines():
            parts = line.split("~")
            brick = []
            for part in parts:
                items = part.split(",")
                for i in items:
                    brick.append(int(i))

            bricks.append(brick)

        bricks.sort(key=lambda x: x[self.Z_START])
        return bricks

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
