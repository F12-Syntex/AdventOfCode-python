import os

class Day6:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        races = self.parseInput()
        total = 0

        for race in races:
            wins = 0
            for speed in range(race[0] + 1):
                seconds = (race[0] - speed)
                distance = seconds * speed
                if distance > race[1]:
                    wins+=1
                    
            if total == 0:
                total = 1
                
            total = wins if total == 0 else total*wins 
        
        return total
        
    def solve_part2(self):
        race = self.parseInput2()
        total = 0
        wins = 0
        
        for speed in range(race[0] + 1):
            seconds = (race[0] - speed)
            distance = seconds * speed
            if distance > race[1]:
                wins+=1
                
        total = wins if total == 0 else total*wins 
        
        return total
    
    def parseInput(self):
        time = list(map(int, self.input_content.split("\n")[0].split(":")[1].split()))
        distance = list(map(int, self.input_content.split("\n")[1].split(":")[1].split()))
        paired_values = [(t, d) for t, d in zip(time, distance)]
        
        return paired_values
    
    def parseInput2(self):
        time = int(self.input_content.split("\n")[0].split(":")[1].replace(" ", ""))
        distance = int(self.input_content.split("\n")[1].split(":")[1].replace(" ", ""))
        
        return time, distance

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day6", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day6()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
