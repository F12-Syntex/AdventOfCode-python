import os

class Day9:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        
        sum = 0
        
        for line in self.input_content.splitlines():
            
            line = list(map(int, line.split(" ")))
            values = [line]
            
            #whlie line is not all zeroes
            while not all(x == 0 for x in line):    
                tmp = []
                
                for i in range(len(line) - 1):
                    diff = line[i+1] - line[i]
                    tmp.append(diff)
                
                values.append(tmp)
                line = tmp
            
            for i in range(len(values) - 2, -1, -1):
                curr_arr = values[i]
                bottom_arr = values[i+1]     

                currValue = curr_arr[-1]
                increment = bottom_arr[-1]
                
                curr_arr.append(currValue + increment)
            
            sum += values[0][-1]            
        
        return sum
    
    def solve_part2(self):
        
        sum = 0
        
        for line in self.input_content.splitlines():
            
            line = list(map(int, line.split(" ")))
            values = [line]
            
            while not all(x == 0 for x in line):    
                tmp = []
                
                for i in range(len(line) - 1):
                    diff = line[i+1] - line[i]
                    tmp.append(diff)
                
                values.append(tmp)
                line = tmp
            
            for i in range(len(values) - 2, -1, -1):
                curr_arr = values[i]
                bottom_arr = values[i+1]     

                currValue = curr_arr[0]
                increment = bottom_arr[0]

                curr_arr.insert(0, currValue - increment)
                
            sum += values[0][0]            
        
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
