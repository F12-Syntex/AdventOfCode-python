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

        workflow = self.input_content.split("\n\n")

        self.rules = workflow[0].split("\n")
        self.data = workflow[1].split("\n")

        res = 0

        for variables in self.data:
            state = self.computeState('in', variables)
            if state[0] == 'A':
                # print(state[1], variables)
                res += self.computeSumOfVariables(state[1])

        return res
    
    def computeSumOfVariables(self, values):

        pairs = values[1:-1].split(',')
        values = dict(pair.split('=') for pair in pairs)
        values = {k: int(v) for k, v in values.items()}
        return sum(values.values())

    def computeState(self, state, variables):

        # print(state, variables)

        for rule in self.rules:
            key = rule.split("{")[0]
            if key == state:
                computed = self.parseInput(variables, rule)
                return self.computeState(computed, variables)
            
        return (state, variables)
                

    def parseInput(self, values, rule):
        rule = rule.split("{")[1].split("}")[0]
        
        pairs = values[1:-1].split(',')
        values = dict(pair.split('=') for pair in pairs)
        values = {k: int(v) for k, v in values.items()}

        for subrule in rule.split(","):
            if ':' in subrule: # conditional
                target = subrule.split(":")[1]
                comparison = subrule.split(":")[0]

                variable = comparison[0]
                operator = comparison[1]
                value = int(comparison[2:])

                # print(values, subrule)

                if operator == '>':
                    if values[variable] > value:
                        return target
                elif operator == '<':
                    if values[variable] < value:
                        return target
                
        return rule.split(",")[-1]
    
    def computeRule(self, rules, data):
        pass
    
    def solve_part2(self):
        return 0

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().rstrip()

        inputFile = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        if not os.path.exists(inputFile):
            content = self.aoc_utils.grab_input().rstrip()
            if content == "ERROR":
                print("ERROR: Could not grab input from Advent of Code.")
                return
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
