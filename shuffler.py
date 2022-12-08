
class Shuffler():
    """ Shuffler class for the MapReduce programming model.
        This class is responsible for collecting, 
        sorting and distributing the output of the mapping.
    """
    @staticmethod
    def __sort_and_hash(word):
        """Sorts the word into alphabetical order and hashes

        Args:
            word (str): Word to be sorted and hashed

        Returns:
            int: Hashed and sorted word
        """
        char_list = list(word)
        sorted_char = sorted(char_list)
        return hash(''.join(sorted_char))

    def __init__(self, mapping):
        assert isinstance(mapping, list), "Mapping is expected to be a list"

        self.__mapping = mapping
        self.__shuffled_mapping = []

    def __form_tuple(self, word, value):
        """Forms the tuple to be stored in the list

        Args:
            word (str): The key from the mapper
            value (int): The value from the mapper

        Returns:
            tuple: tuple of the hashed word, the value and the original key
        """
        return (self.__sort_and_hash(word), value, word)

    
    def shuffle(self):
        """Shuffles the records of the mapping
        """
        assert len(self.__mapping) > 0, "Map from mapper is empty"

        # add the word to form a tuple, hash the key
        self.__mapping = [self.__form_tuple(word, value) for word, value in self.__mapping]

        self.__shuffled_mapping = sorted(self.__mapping, key=lambda x: x[0])

    def get_shuffled_mapping(self):
        return self.__shuffled_mapping

# Driver Code
'''
words = None
with open("test_book.txt", 'r') as f:
    words = f.readlines()
mapper = Mapper(words)
mapper.map()
map = mapper.get()

shuffler = Shuffler(map)
shuffler.shuffle()
'''
