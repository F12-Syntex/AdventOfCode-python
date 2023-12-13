import os

class Day13:
    def __init__(self):
        self.input_content = None
    
    def solve(self, part2):
        total_sum = 0
        patterns = self.input_content.strip().split("\n\n")
        
        for pattern in patterns:
            grid = [list(row) for row in pattern.split("\n")]
            total_sum += self.evaluateRows(grid, part2) + self.evaluateColumns(grid, part2)
            
        return total_sum
    
    def evaluateRows(self, grid, part2):
        res = 0
        columns = len(grid[0])
        rows = len(grid)
        for pivotRow in range(rows - 1):
            errors = 0
            for rowOffset in range(rows):
                top = pivotRow - rowOffset
                bottom = pivotRow + rowOffset + 1
                if top >= 0 and bottom > top and bottom < rows:
                    for c in range(columns):
                        if grid[top][c] != grid[bottom][c]:
                            errors += 1
            if (part2 and errors == 1) or (not part2 and errors == 0):
                res += 100 * (pivotRow + 1)
        return res
        
    def evaluateColumns(self, grid, part2):
        res = 0
        columns = len(grid[0])
        rows = len(grid)
        for pivotCol in range(columns - 1):
            errors = 0
            for colOffset in range(columns):
                left = pivotCol - colOffset
                right = pivotCol + colOffset + 1
                if left >= 0 and right > left and right < columns:
                    for r in range(rows):
                        if grid[r][left] != grid[r][right]:
                            errors += 1
            if (part2 and errors == 1) or (not part2 and errors == 0):
                res += pivotCol + 1
        return res
    
    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "2023", "day13", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day13()
solver.loadInputFiles()
part1_result = solver.solve(False)
part2_result = solver.solve(True)

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
