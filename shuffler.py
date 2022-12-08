from group import Group

class Shuffler():
    """ Shuffler class for the MapReduce programming model.
        This class is responsible for collecting, 
        sorting and distributing the output of the mapping.
    """

    def __init__(self, mapping):
        assert isinstance(mapping, list), "Mapping is expected to be a list"

        self.__mapping = mapping

    def __sort(self):
        pass

    
    def shuffle(self):
        pass
