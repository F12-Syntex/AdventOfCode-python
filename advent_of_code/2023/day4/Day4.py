import os

class Day4:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):

        score = 0
        for line in self.input_content.splitlines():
            input = line.split(":")[1].strip()
            winning = self.convertCardsToList(input.split("|")[0])
            cards = self.convertCardsToList(input.split("|")[1])

            #count how many cards are in the winning set
            winnings = 0
            for card in cards:
                if card in winning:
                    if winnings == 0:
                        winnings = 1
                    else:
                        winnings *= 2

            score += winnings

        return score
    
    def solve_part2(self):
        score = 0
        
        lines = self.input_content.splitlines()
        final_winnings = {}

        for i in range(len(lines)):
            final_winnings[i+1] = 1
        
        def explore_card(line, i, tab=1):

            cardNumber = int(line.split(":")[0].split()[1].strip())
            input = line.split(":")[1].strip()
            winning = self.convertCardsToList(input.split("|")[0])
            cards = self.convertCardsToList(input.split("|")[1])
            woncards = []

            winnings = 0
            for card in cards:
                if card in winning:
                    winnings += 1

            space = ("   " * tab) + " -"
            print(space, lines[i], " - ", cardNumber, " - ", winnings)

            for j in range(i+1, min(i+winnings+1, len(lines))):
                cardN = int(lines[j].split(":")[0].split()[1].strip())
                final_winnings[cardN] = final_winnings[cardN] + 1
                explore_card(lines[j], j, tab+1)


        for i in range(len(lines)):
            line = lines[i]
            explore_card(line, i) 
        
        values = sum(list(final_winnings.values()))

        return values

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
