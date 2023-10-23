from abc import ABC, abstractmethod
import os

class Year2016Day(ABC):

    @abstractmethod
    def part1(self):
        pass
    
    @abstractmethod
    def part2(self):
        pass
    
    def year(self) -> int:
        return 2016

    def getInput(self):
        print(os.getcwd())
