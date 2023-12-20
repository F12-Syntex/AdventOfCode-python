import os

class Day3:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        grid = []
        for line in self.input_content.splitlines():
            grid.append(list(line))
        
        x = 0
        y = 0

        foundNumber = False
        sum = 0
        numbers = []

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                f2 = False
                if grid[y][x].isdigit():
                    numbers.append(grid[y][x])
                    foundNumber = True
                    f2 = True
                
                if (not f2 and foundNumber) or x == len(grid[y]) - 1:
                    foundNumber = False
                    numberStr = "".join(numbers)
                    
                    if numberStr == "":
                        continue

                    number = int(numberStr)

                    startX = x - len(numbers)
                    endX = x - 1
                    startY = y - 1
                    endY = y + 1
                    
                    numbers = []
                    flag = False

                    for j in range(startY, endY + 1):
                        for i in range(startX - 1, endX + 2):
                            if not flag:
                                if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[j]):
                                    continue
                                character = grid[j][i]
                                if not character.isdigit() and character != ".":
                                    sum += number
                                    flag = True

        return sum
    

    def findAdj(self, startX, startY, endX, endY, grid):
        adj = []
        for j in range(startY, endY+1):
            for i in range(startX, endX+1):
                if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[j]):
                    continue
                character = grid[j][i]
                adj.append([j, i])
        return adj
    
    def solve_part2(self):
        grid = []

        for line in self.input_content.splitlines():
            grid.append(list(line))

        sum = 0
        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                if cell == '*':
                    sum += self.findGears(grid, col_index, row_index)

        return sum
    
    def findGears(self, grid, x, y):

        startX = x - 1
        endX = x + 1
        startY = y - 1
        endY = y + 1

        adj = set()
        for j in range(startY, endY+1):
            for i in range(startX, endX+1):
                if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[j]):
                    continue
                character = grid[j][i]
                if character.isdigit():
                    coords = self.findNumberString(grid, i, j)
                    adj.add((coords[0], coords[1], j))

        data = list(adj)

        if len(data) == 2:
            num1 = int(self.build(grid, data[0][0], data[0][1], data[0][2]))
            num2 = int(self.build(grid, data[1][0], data[1][1], data[1][2]))
            return num1 * num2

        return 0
    
    
    def build(self, grid, startX, endX, y):
        num = ""
        for i in range(startX, endX+1):
            num += grid[y][i]
        return num

    def findNumberString(self, grid, x, y):
        if not grid[y][x].isdigit():
            return None
        
        l, r = x-1, x+1
        left, right = "", ""


        #explore left
        while l >= 0:
            if grid[y][l].isdigit():
                left += grid[y][l]
            else:
                break
            l -= 1

        while r < len(grid[y]):
            if grid[y][r].isdigit():
                right += grid[y][r]
            else:
                break
            r += 1

        return [l+1, r-1]

        



    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day3", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day3()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
