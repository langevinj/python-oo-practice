"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Finds words in the dicitionay"""

    def __init__(self, filename):
        """Calls for the creation of a new dictionary list"""
        self.word_list = self.__create_word_list__(filename)

    def __create_word_list__(self, filename):
        """reads the words.txt file and appends each work to a new list, self.list, the list should only contain words"""
        file = open(filename, "r")
        count = 0
        word_list = []
        for line in file:
            cleaned = line.rstrip('\n')
            word_list.append(cleaned)
            count += 1
        file.close()
        print(f'{count} words read')
        return word_list

    def random(self):
        """Chooses a random word from the list"""
        return choice(self.word_list)

    
class SpecialWordFinder(WordFinder):
    """Sub class to work with blank lines and comments in our read in file"""
    
    def __init__(self, filename):
        """Creates a new word list and calls methods from WordFinder class"""
        super().__init__(filename)
        self.word_list = self.__clean_up__()

    def __clean_up__(self):
        """Cleans up any empty lines or comments left over from the word list file"""
        clean_list = []
        for word in self.word_list:
            if not word.startswith('#') and not word == '':
                clean_list.append(word)
        return clean_list
