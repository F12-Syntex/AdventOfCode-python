import os

class Day1:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        print(self.input_content)
        return

    def solve_part2(self):
        pass

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day1", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

    


# Usage example:
solver = Day1()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
