import os
from math import gcd

class Day8:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        
        movements = self.input_content.split("\n")[0].strip()
        movements = list(movements)
        
        paths = self.input_content.split("\n")[2:]
        
        mapping = {}
        start = 'AAA'
        end = 'ZZZ'
        
        for line in paths:
                
            src = line.split(" ")[0]
            
            dest = line[len(src) + 1:]
            l, r = dest.split(',')
            l, r = l.replace("(", ""), r.replace(")", "")
            l, r = l.replace("=", ""), r.replace("=", "")
            l, r = l.strip(), r.strip()
            
            mapping[src] = (l, r)
            
            
        curr = start
        moves = 0
        
        while curr != end:
            movement = movements[moves % len(movements)]
            l, r = mapping[curr]
            
            if movement == 'R':
                curr = r
            elif movement == 'L':
                curr = l

            moves += 1
            
        return moves
    
    def solve_part2(self):
        
        movements = self.input_content.split("\n")[0].strip()
        movements = list(movements)
        
        paths = self.input_content.split("\n")[2:]
        
        mapping = {}
        
        for line in paths:
                
            src = line.split(" ")[0]
            
            dest = line[len(src) + 1:]
            l, r = dest.split(',')
            l, r = l.replace("(", ""), r.replace(")", "")
            l, r = l.replace("=", ""), r.replace("=", "")
            l, r = l.strip(), r.strip()
            
            group = src[len(src) - 1:]
            
            if group not in mapping:
                mapping[group] = {}
            
            mapping[group][src] = (l, r)
            
        moves = 0
        cur = list(mapping['A'].keys())
        res = []
        
        while True:
            currMove = movements[moves % len(movements)]
            
            tmp = []
            
            for index in range(len(cur)):
                i = cur[index]
                values = mapping[i[len(i) - 1:]][i]
                # print(i, values)
                if currMove == 'R':
                    tmp.append(values[1])
                elif currMove == 'L':
                    tmp.append(values[0])
                    
                if i.endswith('Z'):
                    for o in res:
                        if o[0] == index:
                            return self.compute(res)
                    res.append((index, moves))
                    
            cur = tmp
            moves += 1
            
    def compute(self, data):
        
        values = [x[1] for x in data]
        
        #get lcm of all values
        lcm = values[0]
        for i in values[1:]:
          lcm = lcm*i//gcd(lcm, i)
          
        return lcm


    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "Day8", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day8()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
