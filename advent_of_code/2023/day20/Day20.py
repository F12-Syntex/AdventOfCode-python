import collections
import os
import time
from AOCInputGrabber import AOCInputGrabber

class Day20:
    def __init__(self):
        self.input_content = None
        self.DAY = 20
        self.YEAR = 2023
        self.aoc_utils = AOCInputGrabber(self.YEAR, self.DAY)

    def solve_part1(self):

        broadcast = self.get_broadcast()
        self.print_dict(broadcast)

        # modules = self.parseSignals()

        # index = 1
        # queue = collections.deque()
        # queue.append(modules["button"])


        # #TODO deal with % and & modules state
        # while queue:
        #     name, mt, dest, signal, state = queue.popleft()
        #     print(name, "=>", mt, dest, signal, state)
        
        #     if mt == "button":
        #         for d in dest:
        #             print(f"\033[33m{name} -{signal}-> {d}\033[m")
        #             queue.append(modules[d])

        #     if mt == "broadcast":
        #         #There is a single broadcast module (named broadcaster). When it receives a pulse, it sends the same pulse to all of its destination modules.
        #         for d in dest:
        #             print(f"\033[33m{name} -{signal}-> {d}\033[m")
                    
        #     if mt == "%":
        #         if signal == "high":
        #             continue
            
        #         pulse = ""

        #         if state == "off":
        #             state, pulse = "on", "high"
        #         else:
        #             state, pulse = "off", "low"

        #         for d in dest:
        #             print(f"\033[33m{name} -{pulse}-> {d}\033[m")
        #             modules[d] = (modules[d][0], modules[d][1], modules[d][2], pulse, modules[d][4])
        #             queue.append(modules[d])

                
                
            


            # index += 1
            # if index < len(modules):
            #     queue.append(modules[index])


        return 0
    
    def solve_part2(self):
        return 0
    
    def print_dict(self, dict):
        for k, v in dict.items():
            print(k, "=>", v)

    def get_broadcast(self):
        broadcast = {}
        for line in self.input_content.splitlines():
            name, rest = line.split("->")
            mt = "broadcast"
            name = name.strip()
            state = "empty"
            if name.strip() != "broadcaster":
                mt = name[0]
                name = name[1:]
            if mt == "%":
                state = "off"
            if mt == '&':
                state = {} #name of module : most recent signal
            dest = rest.replace(" ", "").split(",")
            broadcast[name] = (name, mt, dest, "low", state)
        
        broadcast["button"] = ("button", "button", ["broadcaster"], "low", "empty")
        return broadcast

    def parseSignals(self):
        modules = {}
        for line in self.input_content.splitlines():
            name, rest = line.split("->")
            mt = "broadcast"
            name = name.strip()
            state = "empty"
            if name.strip() != "broadcaster":
                mt = name[0]
                name = name[1:]
            if mt == "%":
                state = "off"
            if mt == '&':
                state = {} #name of module : most recent signal
            dest = rest.replace(" ", "").split(",")
            modules[name] = (name, mt, dest, "low", state)
        
        modules["button"] = ("button", "button", ["broadcaster"], "low", "empty")

        return modules

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read().rstrip()

        inputFile = os.path.join(os.getcwd(), str(self.YEAR), "day"+str(self.DAY), "input.txt")
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
print("Solution to Part 1:", part1_result, "completed in", round((end_time_part1 - start_time_part1) * 1000), "ms")

start_time_part2 = time.time()
part2_result = solver.solve_part2()
end_time_part2 = time.time()
print("Solution to Part 2:", part2_result, "completed in", round((end_time_part2 - start_time_part2) * 1000), "ms")
