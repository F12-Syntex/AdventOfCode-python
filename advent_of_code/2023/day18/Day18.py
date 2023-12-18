import os

class Day18:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):

        points = [(0, 0)]
        movement = {
            'U': (0, -1),
            'D': (0, 1),
            'L': (-1, 0),
            'R': (1, 0)
        }

        perimeter = 0
        for line in self.input_content.splitlines():
            direction, distance, _ = line.split(" ")
            offset = movement[direction]
            curr = points[-1]
            distance = int(distance)
            perimeter += distance
            nx, ny = (curr[0] + distance * offset[0]), (curr[1] + distance * offset[1])
            points.append((nx, ny))

        area_outside = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2

        return (area_outside - perimeter // 2 + 1) + perimeter
    
    def solve_part2(self):

        points = [(0, 0)]
        movement = {
            '3': (0, -1),
            '1': (0, 1),
            '2': (-1, 0),
            '0': (1, 0)
        }

        perimeter = 0
        for line in self.input_content.splitlines():
            
            offset = movement[line.split(" ")[2][-2]]
            distance = int(line.split(" ")[2][2:-2], 16)

            curr = points[-1]
            distance = int(distance)
            perimeter += distance
            nx, ny = (curr[0] + distance * offset[0]), (curr[1] + distance * offset[1])
            points.append((nx, ny))

        area_outside = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2

        return (area_outside - perimeter // 2 + 1) + perimeter

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day18", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()
            
    def loadGrid(self):
        self.grid = [[c for c in line] for line in self.input_content.split("\n")]
        
    def prettyPrintGrid(self):
        for line in self.grid:
            print(line)


#25681

solver = Day18()
solver.loadInputFiles()

part1_result = solver.solve_part1()
print("Solution to Part 1:", part1_result)

part2_result = solver.solve_part2()
print("Solution to Part 2:", part2_result)
