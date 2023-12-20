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

        res = 0
        for line in self.dataset:
            dataset = self.parseDataset(line)
            if self.accept_item(dataset):
                res += sum(dataset.values())

        return res
    
    def solve_part2(self):
        return self.count_permutations(({key: (1, 4000) for key in "xmas"}))
    
    def count_permutations(self, ranges, name = "in"):
        res = 0

        if name == "R":
            return 0
        
        if name == "A":
            res = 1
            for l, r in ranges.values():
                res *= r - l + 1
            return res
        
        rules, fallback = self.workshops[name]
        for key, comparator, number, target in rules:
            l, r = ranges[key]
            if comparator == "<":
                processing = (l, number - 1)
                skip = (number, r)
            else:
                processing = (number + 1, r)
                skip = (l, number)

            if processing[0] <= processing[1]:
                ranges = dict(ranges)
                ranges[key] = processing
                res += self.count_permutations(ranges, target)
            
            if skip[0] <= skip[1]:
                ranges = dict(ranges)
                ranges[key] = skip
            else:
                break
        else:
            res += self.count_permutations(ranges, fallback)

        return res

    def accept_item(self, item, name = "in"):

            operators = {
                ">": int.__gt__,
                "<": int.__lt__
            }

            if name == "R":
                return False
            if name == "A":
                return True

            rules, fallback = self.workshops[name]
            
            for key, comparator, number, target in rules:
                if operators[comparator](item[key], number):
                    return self.accept_item(item, target)
            
            return self.accept_item(item, fallback)
    
    def parseWorkshops(self, workshop):
        workflow = {}
        for line in workshop:
            name, components = line.split("}")[0].split("{")
            rules = components.split(",")
            workflow[name] = ([], rules.pop()) #rules, target
            for rule in rules:
                comparison, target = rule.split(":")
                key = comparison[0]
                comparitor = comparison[1]
                value = int(comparison[2:])
                workflow[name][0].append((key, comparitor, value, target))
        return workflow

    def parseDataset(self, data):
        dataset = {}
        
        data = data[1:-1].split(",")

        for pair in data:
            key, value = pair.split("=")
            dataset[key] = int(value)
        
        return dataset

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().rstrip()
        
        self.workshops = self.parseWorkshops(self.input_content.split("\n\n")[0].split("\n"))
        self.dataset = self.input_content.split("\n\n")[1].split("\n")

        inputFile = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        if not os.path.exists(inputFile):
            content = self.aoc_utils.grab_input().rstrip()
            if content == "ERROR":
                print("ERROR: Could not grab input from Advent of Code.")
                return
            with open(inputFile, "w") as f:
                f.write(content)

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
