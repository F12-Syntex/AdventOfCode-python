import os
from collections import Counter

class Day7:
    def __init__(self):
        self.input_content = None
    
    def solve(self, sortFunc):
        cards = []
        
        for line in self.input_content.splitlines():
            data = line.split(" ")
            cards.append((data[0], data[1]))
            
        cards = sorted(cards, key=lambda c:sortFunc(c[0]))

        sum = 0
        for i in range(len(cards)):
            sum += (i+1) * int(cards[i][1])
        
        return sum
    
    def formatCards(self, card, part1):
        
        #place joker as the weakest card for part2 otherwise keep it as a strong card for part 1
        Jvalue = chr(ord('9')+2) if part1 else chr(ord('0'))
        
        card = card.replace('J', Jvalue)
        card = card.replace('T', chr(ord('9')+1))
        card = card.replace('Q', chr(ord('9')+3))
        card = card.replace('K', chr(ord('9')+4))
        card = card.replace('A', chr(ord('9')+5))
        return card
    
    
    def sortCards(self, values, card):
        if values == [5]:
            return (6, card)
        
        if values == [1, 4]:
            return (5, card)
        
        if values == [2, 3]:
            return (4, card)
        
        if values == [1, 1, 3]:
            return (3, card)
        
        if values == [1, 2, 2]:
            return (2, card)
        
        if values == [1, 1, 1, 2]:
            return (1, card)
        
        if values == [1, 1, 1, 1, 1]:
            return (0, card)
        
    def sorterA(self, card):
        
        card = self.formatCards(card, True)
        
        counter = Counter(card)
        values = sorted(list(counter.values()))
        return self.sortCards(values, card)
        
    def sorterB(self, card):
        
        card = self.formatCards(card, False)
        
        counter = Counter(card)
        counter2 = Counter(card)
        
        target = 0
        for k in counter:
            if k != '0':
                target = max(target, counter[k])

        if '0' in counter:
            for k in counter:
                if counter[k] == target and k!='0':
                    counter2[k] += counter['0']
                    del counter2['0']
                    break

        counter = counter2
        values = sorted(counter.values())
        
        return self.sortCards(values, card)

    def solve_part1(self):
        return self.solve(self.sorterA)
    
    def solve_part2(self):
        return self.solve(self.sorterB)
    

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day7", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day7()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)