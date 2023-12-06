import os

class Day6:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        return 0
    
    def solve_part2(self):
        return self.input_content

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day6", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day6()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
