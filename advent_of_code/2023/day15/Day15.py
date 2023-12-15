import os

class Day15:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        return sum(self.hash(word) for word in self.input_content.split(","))

    def hash(self, word):
        cres = 0
        for c in word:
            cres += ord(c)
            cres *= 17
            cres %= 256
        return cres
    
    def solve_part2(self):
        mapping = {}
        for word in self.input_content.split(","):
            if '=' in word:
                label, value = word.split("=")
                box = self.hash(label)
                data = (label, value)
                
                
                if box not in mapping:
                    mapping[box] = [data]
                    continue
            
                flag = any(item[0] == label for item in mapping[box]) 
                
                if not flag:
                    mapping[box].append(data)
                    continue
                
                for index in range(len(mapping[box])):
                    if mapping[box][index][0] == label:
                        mapping[box][index] = data
                        break
                
            
            if '-' in word:
                label = word.split("-")[0]
                box = self.hash(label)
                
                if box in mapping:
                    mapping[box] = [item for item in mapping[box] if item[0] != label]
        
        res = 0
        for key in mapping:
            for slot, item in enumerate(mapping[key]):
                res += (1+int(key))*(1+slot)*int(item[1])
                
        return res

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day15", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)

solver = Day15()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)
