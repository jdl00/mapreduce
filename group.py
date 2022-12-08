from dataclasses import dataclass

@dataclass
class Group:
    __hash_value: int
    __anagrams: list

    def __init__(self, hash_value, word) -> None:
        """Creates an instance of a group

        Args:
            hash_value (int): Hash value of the word
            word (str): Word to be added to anagrams
        """
        assert isinstance(hash_value, int), "Hash value is not an integer"
        assert isinstance(word, str), "Word is not a string"

        self.__anagrams.append(word)
        self.__hash_value = hash_value

    @property 
    def count(self) -> int:
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

    @property
    def hash_value(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__hash_value

    def add(self, word):
        """Adds word to the anagram list

        Args:
            word (str): Adds the word to the anagram list
        """
        self.__anagrams.append(word)

    



