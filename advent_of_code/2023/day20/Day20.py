import collections
import math
import os
import time

from AOCInputGrabber import AOCInputGrabber
from Module import Module


class Day20:
    def __init__(self):
        self.input_content = None
        self.DAY = 20
        self.YEAR = 2023
        self.aoc_utils = AOCInputGrabber(self.YEAR, self.DAY)

    def solve_part1(self):
        modules = {}
        broadcast_targets = []

        for line in self.input_content.splitlines():
            left, right = line.strip().split(" -> ")
            outputs = right.split(", ")
            if left == "broadcaster":
                broadcast_targets = outputs
            else:
                type = left[0]
                name = left[1:]
                modules[name] = Module(name, type, outputs)

        for name, module in modules.items():
            for output in module.outputs:
                if output in modules and modules[output].type == "&":
                    modules[output].memory[name] = "lo"

        pulses = [0, 0]

        for _ in range(1000):
            pulses[0] += 1
            q = collections.deque([("broadcaster", x, "lo") for x in broadcast_targets])

            while q:
                origin, target, pulse = q.popleft()

                if pulse == "lo":
                    pulses[0] += 1
                else:
                    pulses[1] += 1

                if target not in modules:
                    continue

                module = modules[target]

                if module.type == "%":
                    if pulse == "lo":
                        module.memory = "on" if module.memory == "off" else "off"
                        outgoing = "hi" if module.memory == "on" else "lo"
                        for x in module.outputs:
                            q.append((module.name, x, outgoing))
                else:
                    module.memory[origin] = pulse
                    outgoing = (
                        "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                    )
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))

        return pulses[0] * pulses[1]

    def solve_part2(self):
        modules = {}
        broadcast_targets = []

        for line in self.input_content.splitlines():
            left, right = line.strip().split(" -> ")
            outputs = right.split(", ")
            if left == "broadcaster":
                broadcast_targets = outputs
            else:
                type = left[0]
                name = left[1:]
                modules[name] = Module(name, type, outputs)

        for name, module in modules.items():
            for output in module.outputs:
                if output in modules and modules[output].type == "&":
                    modules[output].memory[name] = "lo"

        (feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

        cycle_lengths = {}
        seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

        presses = 0

        while True:
            presses += 1
            q = collections.deque([("broadcaster", x, "lo") for x in broadcast_targets])
            
            while q:
                origin, target, pulse = q.popleft()
                
                if target not in modules:
                    continue
                
                module = modules[target]
                
                if module.name == feed and pulse == "hi":
                    seen[origin] += 1

                    if origin not in cycle_lengths:
                        cycle_lengths[origin] = presses
                    else:
                        assert presses == seen[origin] * cycle_lengths[origin]
                        
                    if all(seen.values()):
                        x = 1
                        for cycle_length in cycle_lengths.values():
                            x = x * cycle_length // math.gcd(x, cycle_length)
                        return x
                        exit(0)
                
                if module.type == "%":
                    if pulse == "lo":
                        module.memory = "on" if module.memory == "off" else "off"
                        outgoing = "hi" if module.memory == "on" else "lo"
                        for x in module.outputs:
                            q.append((module.name, x, outgoing))
                else:
                    module.memory[origin] = pulse
                    outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))

    def loadInputFiles(self):
        inputPath = os.path.join(
            os.getcwd(), str(self.YEAR), f"day{str(self.DAY)}", "input.txt"
        )
        with open(inputPath, "r") as f:
            self.input_content = f.read().rstrip()

        inputFile = os.path.join(
            os.getcwd(), str(self.YEAR), f"day{str(self.DAY)}", "input.txt"
        )
        if not os.path.exists(inputFile):
            content = self.aoc_utils.grab_input().rstrip()
            if content == "ERROR":
                print("Error grabbing input")
                return
            with open(inputFile, "w") as f:
                f.write(content)


solver = Day20()
solver.loadInputFiles()

start_time_part1 = time.time()
part1_result = solver.solve_part1()
end_time_part1 = time.time()
print(
    "Solution to Part 1:",
    part1_result,
    "completed in",
    round((end_time_part1 - start_time_part1) * 1000),
    "ms",
)

start_time_part2 = time.time()
part2_result = solver.solve_part2()
end_time_part2 = time.time()
print(
    "Solution to Part 2:",
    part2_result,
    "completed in",
    round((end_time_part2 - start_time_part2) * 1000),
    "ms",
)
