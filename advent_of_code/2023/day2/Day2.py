import os

class Day2:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        sum = 0
        for line in self.input_content.splitlines():
            count = [0, 0, 0]
            id = int(line.split(":")[0].split(" ")[1])

            line = line.split(":")[1]
            for games in line.split(";"):
                entries = games.split(",")
                for entry in entries:
                    entry = entry.strip()
                    curr = int(entry.split(" ")[0])
                    colour = entry.split(" ")[1]

                    if colour == "red":
                        count[0] = max(count[0], curr)
                    elif colour == "green":
                        count[1] = max(count[1], curr)
                    elif colour == "blue":
                        count[2] = max(count[2], curr)
            
            if(count[0] <= 12 and count[1] <= 13 and count[2] <= 14):
                sum += id

        return sum

    def solve_part2(self):
        sets = []
        for line in self.input_content.splitlines():
            count = [0, 0, 0]
            id = int(line.split(":")[0].split(" ")[1])

            line = line.split(":")[1]
            for games in line.split(";"):
                entries = games.split(",")
                for entry in entries:
                    entry = entry.strip()
                    curr = int(entry.split(" ")[0])
                    colour = entry.split(" ")[1]

                    if colour == "red":
                        count[0] = max(count[0], curr)
                    elif colour == "green":
                        count[1] = max(count[1], curr)
                    elif colour == "blue":
                        count[2] = max(count[2], curr)
            
            sets.append(count)
        
        sum = 0
        for i in range(len(sets)):
            curr = sets[i]
            power = sets[i][0] * sets[i][1] * sets[i][2]
            sum += power



        return sum

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day2", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

# Usage example:
solver = Day2()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
