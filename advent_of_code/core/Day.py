from abc import ABC, abstractmethod
import os

class Day(ABC):

    @abstractmethod
    def part1(self):
        pass
    
    @abstractmethod
    def part2(self):
        pass
    
    @abstractmethod
    def year(self) -> int:
        pass

    def getInput(self):
        print(os.getcwd())