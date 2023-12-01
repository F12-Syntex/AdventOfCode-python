import os

class Day1:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        floor = 0
        for char in self.input_content:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

        return floor

    def solve_part2(self):
        floor = 0
        count = 0
        for char in self.input_content:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
            count += 1

            if floor == -1:
                return count
        
        return floor

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2015", "day1", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

    


# Usage example:
solver = Day1()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
