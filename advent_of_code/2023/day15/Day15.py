import os


# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

class Day15:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        res = 0
        for word in self.input_content.split(","):
            res += self.hash(word)
            
        return res

    def hash(self, word):
        cres = 0
        for c in word:
            cres += ord(c)
            cres *= 17
            cres %= 256
        return cres
    
    def solve_part2(self):
        res = 0
        mapping = {}
        for word in self.input_content.split(","):
            if '=' in word:
                label, value = word.split("=")
                box = self.hash(label)
                
                data = (label, value)
                
                if box not in mapping:
                    mapping[box] = [data]
                else:
                    arr = mapping[box]
                    flag = False
                    index = 0
                    for item in arr:
                        if item[0] == label:
                            mapping[box][index] = data
                            flag = True
                        index += 1
                    
                    if not flag:
                        arr.append(data)
                        
                    mapping[box] = arr
            
            if '-' in word:
                label, value = word.split("-")
                
                box = self.hash(label)
                if box in mapping:
                    arr = mapping[box]
                    for item in arr:
                        if item[0] == label:
                            arr.remove(item)
                    mapping[box] = arr
            # print(mapping)    
        
        for key in mapping:
            arr = mapping[key]
            for slot in range(len(arr)):
                item = arr[slot]
                focus = (1+int(key))*(1+int(slot))*int(item[1])
                # print((1+key), " * ", (1+slot), " * ", item[1], " = ", focus)
                res += focus
                
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
