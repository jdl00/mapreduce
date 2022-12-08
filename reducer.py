from group import Group

class Reducer():
    """Reducer reieves the mapping of hashed key and (key,value)
       It then applies the logic to reduce the map to only include
       acronyms
    """

    def __init__(self, shuffled_map):
        """Creates an instance of the reducer

        Args:
            shuffled_map (list): The shuffled map from the shuffler
        """
        assert isinstance(shuffled_map, list), "Shuffled map is not a list"
        assert len(shuffled_map) > 0, "Shuffled map passed is empty"

        self.__shuffled_map = shuffled_map
        self.__grouped_records = []

    def reduce(self):
        # Get the Front of the maps hash, and create the first group
        current_hash, _, key = self.__shuffled_map[0]
        new_group = Group(key)
        self.__grouped_records.append(new_group)

        map_idx = 0
        for hash, _, key in self.__shuffled_map:
            if hash != current_hash:
                map_idx += 1
                new_group = Group(key)
                self.__grouped_records.append(new_group)
                current_hash = hash
                continue
            self.__grouped_records[map_idx].add(key)
        
        new_list = []
        for group in self.__grouped_records:
            if group.count > 1:
                new_list.append(group)
        self.__grouped_records = new_list
                
    def output(self):
        for group in self.__grouped_records:
            print(group.anagrams)


