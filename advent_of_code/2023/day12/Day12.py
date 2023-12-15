import collections
import os

class Day12:
    def __init__(self):
        self.input_content = None
        self.cache = {}
        
    def solve_part1(self):
        res = 0

        for line in self.input_content.splitlines():
            onsens, groups = line.split()
            groups = tuple(map(int, groups.split(",")))
            
            res += self.permutations(onsens, groups)

        return res
    
    def solve_part2(self):
        res = 0

        for line in self.input_content.splitlines():
            onsens, groups = line.split()
            groups = tuple(map(int, groups.split(",")))
            
            onsens = "?".join([onsens] * 5)
            groups *= 5
            
            res += self.permutations(onsens, groups)
    
        return res
    
    def permutations(self, onsens, groups):
        
        res = 0
        #base case if onsens are empty
        if onsens == "":
            return 1 if groups == () else 0
        
        #base case if groups are empty
        if groups == ():
            return 1 if "#" not in onsens else 0
        
        key = (onsens, groups)
        
        if key in self.cache:
            return self.cache[key]
        
        #pretend a dot is a question mark
        if onsens[0] in "?.":
            res += self.permutations(onsens[1:], groups)
        
        #pretend a dot is a pound
        if onsens[0] in "#?":
            if groups[0] <= len(onsens) and "." not in onsens[:groups[0]] and (groups[0] == len(onsens) or onsens[groups[0]] != "#"):
                res += self.permutations(onsens[groups[0] + 1:], groups[1:])
            
        self.cache[key] = res
        
        return res

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day12", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
        
        self.grid = [[character for character in self.input_content] for line in self.input_content.splitlines()]

solver = Day12()
solver.loadInputFiles()
part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)
