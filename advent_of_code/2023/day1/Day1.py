import os

class Day1:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        sum = 0 

        for line in self.input_content.splitlines():
            leftNumber = "-1" 
            rightNumber = "-1" 

            l = len(line) - 1
            for r in range(len(line)):
                
                if line[r].isdigit() and leftNumber == "-1":
                    leftNumber = line[r]
                
                if line[l].isdigit() and rightNumber == "-1":
                    rightNumber = line[l]
                l -= 1

            if leftNumber != "-1" and rightNumber != "-1": 
                joinedNum = leftNumber + rightNumber
                joinedNum = int(joinedNum)
                sum += joinedNum

        return sum

    def solve_part2(self):
        sum = 0 

        for line in self.input_content.splitlines():
            leftNumber = "-1" 
            rightNumber = "-1" 

            l = len(line) - 1
            for r in range(len(line)):

                left = self.convertStringToNumber(line[0:r+1])
                right = self.convertStringToNumber(line[l:len(line)])

                if line[r].isdigit():
                    left = line[r]
                
                if line[l].isdigit():
                    right = line[l]

                if left[0].isdigit() and leftNumber == "-1":
                    leftNumber = left[0]
                
                if right[0].isdigit() and rightNumber == "-1":
                    rightNumber = right[0]
                    
                l -= 1

            if leftNumber != "-1" and rightNumber != "-1": 
                joinedNum = leftNumber + rightNumber
                joinedNum = int(joinedNum)
                sum += joinedNum

        return sum

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day1", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

    
    def convertStringToNumber(self, string):
        if "one" in string:
            return str(1)
        if "two" in string:
            return str(2)
        if "three" in string:
            return str(3)
        if "four" in string:
            return str(4)
        if "five" in string:
            return str(5)
        if "six" in string:
            return str(6)
        if "seven" in string:
            return str(7)
        if "eight" in string:
            return str(8)
        if "nine" in string:
            return str(9)
        return " "
    


# Usage example:
solver = Day1()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
