import os
import time
from AOCInputGrabber import AOCInputGrabber

class Day19:
    def __init__(self):
        self.input_content = None
        self.DAY = 19
        self.YEAR = 2023
        self.aoc_utils = AOCInputGrabber(self.YEAR, self.DAY)

    def solve_part1(self):
        self.loadGrid()
        self.prettyPrintGrid()
        
        return 0
    
    def solve_part2(self):
        return 0

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "test.txt")
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

solver = Day19()
solver.loadInputFiles()

start_time_part1 = time.time()
part1_result = solver.solve_part1()
end_time_part1 = time.time()
print("Solution to Part 1:", part1_result, "completed in", round((end_time_part1 - start_time_part1) * 1000), "ms")

start_time_part2 = time.time()
part2_result = solver.solve_part2()
end_time_part2 = time.time()
print("Solution to Part 2:", part2_result, "completed in", round((end_time_part2 - start_time_part2) * 1000), "ms")
