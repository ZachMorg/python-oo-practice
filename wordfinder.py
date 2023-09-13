"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self,directory):
        self.directory = open(directory)
        self.list = self.read()
        self.num_words = len(self.list)

        print(f'{self.num_words} words read')
    
    def read(self):
        return [line.strip() for line in self.directory]

    def random(self):
        print (self.list[random.randint(0, self.num_words-1)])



class SpecialWordFinder (WordFinder):
    def __init__(self,directory):
        super().__init__(directory)

    def read(self):
        return [line.strip() for line in self.directory
            if '#' not in line and line.strip()]
    