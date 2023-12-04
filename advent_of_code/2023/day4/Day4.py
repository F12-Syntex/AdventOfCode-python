import os

class Day4:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):

        score = 0
        for line in self.input_content.splitlines():
            winning, cards = self.parseLine(line)

            winnings = len(set(winning).intersection(set(cards)))
            
            if winnings == 0:
                continue

            score += 2 ** (winnings - 1)
            
        return score
    
    def solve_part2(self):
        lines = self.input_content.splitlines()
        final_winnings = {}

        for i in range(len(lines)):
            final_winnings[i+1] = 1
        
        def explore_card(i):
            line = lines[i]
            winning, cards = self.parseLine(line)

            winnings = len(set(winning).intersection(set(cards)))

            for j in range(i+1, min(i+winnings+1, len(lines))):
                final_winnings[j + 1] += 1 #j+1 is the card number
                explore_card(j)


        for i in range(len(lines)):
            explore_card(i) 
        
        values = sum(list(final_winnings.values()))

        return values

    def parseLine(self, line):
        input = line.split(":")[1].strip()

        winning = []
        cards = []

        winningCards = input.split("|")[0]
        for card in winningCards.split():
            winning.append(card.strip())

        userCards = input.split("|")[1]
        for card in userCards.split():
            cards.append(card.strip())

        return winning, cards

    def convertCardsToList(self, cards):
        cardsList = []
        for card in cards.split():
            cardsList.append(card.strip())
        return cardsList

    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day4", "test.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day4()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
