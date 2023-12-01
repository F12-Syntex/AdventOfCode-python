import os
class Day1:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):

        sum = 0

        for line in self.input_content.splitlines():
            dimentions = line.split("x")
            l = int(dimentions[0])
            w = int(dimentions[1])
            h = int(dimentions[2])

            side1 = l*w
            side2 = w*h
            side3 = h*l

            sum += 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)

        return sum

    def solve_part2(self):

        sum = 0

        for line in self.input_content.splitlines():
            dimentions = line.split("x")
            l = int(dimentions[0])
            w = int(dimentions[1])
            h = int(dimentions[2])

            smallest = sorted([l, w, h])

            sum += 2*smallest[0] + 2*smallest[1] + l*w*h

        return sum

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2015", "day2", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

# Usage example:
solver = Day1()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
