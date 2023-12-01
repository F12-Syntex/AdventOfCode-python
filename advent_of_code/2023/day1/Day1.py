import os

class Day1:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):

        sum = 0

        for line in self.input_content.splitlines():
            #fins the first number in the string starting from the left

            firstNum = None
            secondNum = None

            for i in range(len(line)):
                if line[i].isdigit():
                    first_num = line[i]
                    break

            
            #finds the second number in the string starting from the right
            for i in range(len(line)-1, -1, -1):
                if line[i].isdigit():
                    second_num = line[i]
                    break
            
            joinedNum = first_num + "" + second_num

            #converts the joined number to an integer
            joinedNum = int(joinedNum)
            sum += joinedNum


        return sum

    def solve_part2(self):

        sum = 0

        for line in self.input_content.splitlines():
            #fins the first number in the string starting from the left

            firstNum = None
            secondNum = None

            for i in range(len(line)):
                #make a string from index 0 to this index
                substring = line[0:i+1]
                
                if "one" in substring:
                    first_num = str(1)
                    break
                if "two" in substring:
                    first_num = str(2)
                    break
                if "three" in substring:
                    first_num = str(3)
                    break
                if "four" in substring:
                    first_num = str(4)
                    break
                if "five" in substring:
                    first_num = str(5)
                    break
                if "six" in substring:
                    first_num = str(6)
                    break
                if "seven" in substring:
                    first_num = str(7)
                    break
                if "eight" in substring:
                    first_num = str(8)
                    break
                if "nine" in substring:
                    first_num = str(9)
                    break
                

                if line[i].isdigit():
                    first_num = line[i]
                    break
            
            
            #finds the second number in the string starting from the right
            for i in range(len(line)-1, -1, -1):

                substring = line[i:len(line)]

                if "one" in substring:
                    second_num = str(1)
                    break
                if "two" in substring:
                    second_num = str(2)
                    break
                if "three" in substring:
                    second_num = str(3)
                    break
                if "four" in substring:
                    second_num = str(4)
                    break
                if "five" in substring:
                    second_num = str(5)
                    break
                if "six" in substring:
                    second_num = str(6)
                    break
                if "seven" in substring:
                    second_num = str(7)
                    break
                if "eight" in substring:
                    second_num = str(8)
                    break
                if "nine" in substring:
                    second_num = str(9)
                    break

                if line[i].isdigit():
                    second_num = line[i]
                    break

            joinedNum = first_num + "" + second_num

            #converts the joined number to an integer
            joinedNum = int(joinedNum)
            sum += joinedNum


        return sum

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day1", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

    


# Usage example:
solver = Day1()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
