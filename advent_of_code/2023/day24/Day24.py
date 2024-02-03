import os
import time
from AOCInputGrabber import AOCInputGrabber
from Hellstones import Hellstones
import sympy

class Day24:
    def __init__(self):
        self.input_content = None
        self.DAY = 24
        self.YEAR = 2023
        self.aoc_utils = AOCInputGrabber(self.YEAR, self.DAY)

    def solve_part1(self):

        hellstones = []
        for line in self.input_content.splitlines():
            hellstones.append(Hellstones(*map(int, line.replace("@", ",").split(","))))
        

        res = 0
        for i in range(len(hellstones)):
            for j in range(i + 1, len(hellstones)):
                hs1, hs2 = hellstones[i], hellstones[j]
                if hs1.intersects(hs2):
                    a1, b1, c1 = hs1.a, hs1.b, hs1.c
                    a2, b2, c2 = hs2.a, hs2.b, hs2.c
                    
                    x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1)
                    y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)

                    if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                        if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0 for hs in (hs1, hs2)):
                            res += 1
        
        return res

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().rstrip()

        inputFile = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
        if not os.path.exists(inputFile):
            content = self.aoc_utils.grab_input().rstrip()
            with open(inputFile, "w") as f:
                f.write(content)

    def solve_part2(self):
        hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in self.input_content.splitlines()]

        xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

        equations = []

        for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
            equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
            equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
            if i < 2:
                continue
            answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
            if len(answers) == 1:
                break
            

        answer = answers[0]

        return answer[xr] + answer[yr] + answer[zr]

solver = Day24()
solver.loadInputFiles()

start_time_part1 = time.time()
part1_result = solver.solve_part1()
end_time_part1 = time.time()
print("Solution to Part 1:", part1_result, "completed in", round((end_time_part1 - start_time_part1) * 1000), "ms")

start_time_part2 = time.time()
part2_result = solver.solve_part2()
end_time_part2 = time.time()
print("Solution to Part 2:", part2_result, "completed in", round((end_time_part2 - start_time_part2) * 1000), "ms")
