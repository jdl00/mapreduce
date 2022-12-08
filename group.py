from dataclasses import dataclass

@dataclass
class Group:
    __anagrams: list

    def __init__(self, word):
        """Creates an instance of a group

        Args:
            hash_value (int): Hash value of the word
            word (str): Word to be added to anagrams
        """
        assert isinstance(word, str), "Word is not a string"
        self.__anagrams = []
        self.__anagrams.append(word)

    @property 
    def count(self):
        """Gets the number of anagrams 

        Returns:
            int: The amount of anagrams
        """
        return len(self.__anagrams)

    @property 
    def anagrams(self):
        """Returns the anagrams stored

        Returns:
            list: list of anagrams
        """
        return self.__anagrams


    def add(self, word):
        """Adds word to the anagram list

        Args:
            word (str): Adds the word to the anagram list
        """
        self.__anagrams.append(word)

    



