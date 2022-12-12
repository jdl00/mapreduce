from re import findall, sub
from json import load

class Mapper():
    """ Mapper class for the MapReduce programming model.
        This class is responsible for performing the mapping 
        of keys to value, for use by the shuffler.
    """
    # Regex for only letters
    CONST_RE_WORDS = r'[a-zA-Z]'

    # Regex for only symbols
    CONST_RE_SYMBOLS = r'[^\w\s]'

    CONST_RE_NEWLINE= r'\n'

    def __init__(self, lines):
        """Initialises an instance of the mapper

        Args:
            words (list): List of words
        """
        assert isinstance(lines, list), "Expected type of data is a list"
        
        self.__words = ""
        self.__lines = lines
        self.__map = []
        self.__stop_words = []

        with open("stop_words.json", "r") as f:
            self.__stop_words = load(f)

    def __final_word_checks(self, word):
        if not word: return False

        if word in self.__stop_words: return False

        if len(word) < 2: return False

        return True
        

    
    def __clean(self):
        """ Cleans the list of words, so that they are all just natural words
        """
        assert len(self.__lines) > 0, "Expected to be filled with lines from the txt"

        # We also want to clean the stop words to allow proper comparison
        self.__stop_words = [sub(self.CONST_RE_SYMBOLS, "", word) for word in self.__stop_words]

        # Replace all newlines with a space to mark for splitting
        lines = [line.replace("\n"," ") for line in self.__lines]

        # Replace symbols such as '-' with spaces to seperate
        lines = [sub(self.CONST_RE_SYMBOLS, " ", line) for line in lines]

        # Form a string of all the lines
        temp_str = "".join(lines) 

        # Split by spaces to just get words
        split_words = temp_str.split(' ')
       
        # Extract out only the words in the string 
        split_words = [''.join(findall(self.CONST_RE_WORDS, word)) for word in split_words]

        # Removes empty elements and converts all the elements to lower case
        # as well as removing single letters

        # as well as removing single letters
        split_words = [word.lower() for word in split_words if self.__final_word_checks(word)]

        #split_words = [word.lower() for word in split_words if word and len(word) > 1]

        # Remove all the words in the stop words list
        #split_words = [word for word in split_words if not word in self.__stop_words]
        
        # Removes duplicated words and stores to the words variable
        unique_set = set(split_words)
        self.__words = list(unique_set)

    def map(self):
        """Maps the words to a pair, where the key is the word, and the value is 1
        """
        assert isinstance(self.__map, list), "Mapper members has changed from a list"

        # Clean the split words list
        self.__clean()

        # Check if the clean funtion executed correctly 
        assert len(self.__words) > 0, "Word list is empty"

        #Form the map
        self.__map = [(word, 1) for word in self.__words]

    def get(self):
        """Returns the map from the mapper

        Returns:
            list: The map of words to 1
        """
        assert len(self.__map) > 0, "Get should only be called once map has been called"        

        return self.__map
