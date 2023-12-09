import os

class Day9:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        return self.solve(True)
    
    def solve_part2(self):
        return self.solve(False)
    
    def solve(self, part1): 
        sum = 0
        
        for line in self.input_content.splitlines():
            values = [line := [int(x) for x in line.split(" ")]]
            
            while any(line := [j - i for i, j in zip(line, line[1:])]):
                values.append(line)
            
            increment = 0
            for i in range(len(values) - 2, -1, -1):
                index = -1 if part1 else 0
                increment = values[i][index] + (-values[i+1][index] if not part1 else values[i+1][index])
                values[i].append(increment) if part1 else values[i].insert(0, increment)
            sum += increment
 
        return sum

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day9", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day9()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
