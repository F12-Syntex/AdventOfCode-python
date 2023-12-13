import os

class Day12:
    def __init__(self):
        self.input_content = None
    
    def verify(self, dots, blocks):
        curr = 0
        visited = []
        for character in dots:
            if character == ".":
                if curr > 0:
                    visited.append(curr)
                curr = 0
            elif character == "#":
                curr += 1
            else:
                assert False
        
        if curr > 0:
            visited.append(curr)
        
        return visited == blocks
    
    def find(self, dots, blocks, index):
        if index == len(dots):
            return 1 if self.verify(dots, blocks) else 0
        if dots[index] == "?":
            return (self.find(dots[:index] + "#" + dots[index+1:], blocks, index + 1) + 
                    self.find(dots[:index] + "." + dots[index+1:], blocks, index + 1))
        else:
            return self.find(dots, blocks, index + 1)
        
    def solve_part1(self):
        res = 0
        for line in self.input_content.splitlines():
            springs = line.split(" ")[0]
            groups = list(map(int, line.split(" ")[1].split(",")))
            
            score = self.find(springs, groups, 0)
            res += score
        return res
    
    def solve_part2(self):
        return 0

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day12", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
        
        self.grid = [[character for character in self.input_content] for line in self.input_content.splitlines()]

solver = Day12()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
