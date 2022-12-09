
class Shuffler():
    """ Shuffler class for the MapReduce programming model.
        This class is responsible for collecting, 
        sorting and distributing the output of the mapping.
    """

    def __init__(self, mapping):
        assert isinstance(mapping, list), "Mapping is expected to be a list"

        self.__mapping = mapping
        self.__shuffled_mapping = []

    @staticmethod
    def __sort_and_hash(word):
        """Sorts the word into alphabetical order and hashes

        Args:
            word (str): Word to be sorted and hashed

        Returns:
            int: Hashed and sorted word
        """
        assert isinstance(word, str), "Word is expected to be a string"

        # Sort the key
        char_list = list(word)
        sorted_char = sorted(char_list)

        # Return the hashed, sorted key
        return hash(''.join(sorted_char))

    def __form_tuple(self, word, value):
        """Forms the tuple to be stored in the list

        Args:
            word (str): The key from the mapper
            value (int): The value from the mapper

        Returns:
            tuple: tuple of the hashed word, the value and the original key
        """
        assert isinstance(word, str), "Word is expected to be a string"
        assert isinstance(value, int), "Value is expected to be a int"

        return (self.__sort_and_hash(word), value, word)

    
    def shuffle(self):
        """Shuffles the records of the mapping
        """
        assert len(self.__mapping) > 0, "Map from mapper is empty"

        # Add the word to form a tuple, hash the key
        self.__mapping = [self.__form_tuple(word, value) for word, value in self.__mapping]

        # Sort the mapping using the hashed value
        self.__shuffled_mapping = sorted(self.__mapping, key=lambda x: x[0])

    def get_shuffled_mapping(self):
        """Gets the shuffled mapping

        Returns:
            list: The mapping after the shuffler
        """
        assert isinstance(self.__shuffled_mapping, list), "Shuffled mapping isnt a list"
        assert len(self.__shuffled_mapping) > 0, "Shuffled mapping is empty"

        return self.__shuffled_mapping