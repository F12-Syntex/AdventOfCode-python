import os
class Day12:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        for line in self.input_content.splitlines():
            
            springs = line.split(" ")[0]
            groups = list(map(int, line.split(" ")[1].split(",")))
        
            self.expandSprings(springs, groups)
            
            
            exit()
        
        return 0
    
    def expandSprings(self, springs, groups):
        for contiguous_length in groups:
            groupedData = self.groupData(springs)
            # print()
            subsets = []
            for group in groupedData:
                # print(springs, group, contiguous_length)
                # print(group)
                permutations = self.permute(group, contiguous_length)
                subsets.append(permutations)
                # print("\t-",permutations)
            flatten = self.flatten(subsets)
            print(flatten)

            exit()
            
            
    def flatten(self, subsets):
        result = []
        for sub_array in subsets:
            if not sub_array:
                result.append(['.' * len(subsets[0][0])])
            else:
                new_sub_array = [''.join(entry) for entry in sub_array]
                result.append(new_sub_array)
        return result


    
    def permute(self, group, contiguous_length):
        res = set()
        for l in range(len(group) - contiguous_length + 1):
            tmp, c = [], sum(1 for element in group if element == '#')
            # print(l)
            for r in range(len(group)):
                # print("\t", r, c, tmp, c, contiguous_length, group[l], r >= l, group)
                if group[l] == '?' and c < contiguous_length and r >= l:
                    c+=1
                    tmp.append("#")
                else:
                    tmp.append(group[r])
            res.add(tuple(tmp))
        
        return list(res)
                
    
    def groupData(self, springs):
        res = []
        tmp = []
        for spring in springs:
            if spring == '.':
                if tmp:
                    res.append(tmp)
                tmp = []
                res.append(tmp)
            else:
                tmp.append(spring)
        if tmp:
            res.append(tmp)
        return res
        
    
    def solve_part2(self):
        return 0

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day12", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day12()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
