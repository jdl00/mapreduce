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
        """Reduce the map to only anagrams, and create the groups
        """
        assert not self.__grouped_records, "List has already been reduced"

        # Get the Front of the maps hash, and create the first group
        current_hash, _, key = self.__shuffled_map[0]
        new_group = Group(key)
        self.__grouped_records.append(new_group)

        # Setup an index for adding anagrams
        map_idx = 0
        for idx, (hash, _, key) in enumerate(self.__shuffled_map):
            # Skip the first record as we've already added it
            if idx == 0: continue

            # If the hash changes add a new group and update the index
            if hash != current_hash:
                map_idx += 1
                new_group = Group(key)
                self.__grouped_records.append(new_group)
                current_hash = hash
                continue

            # Add the word to the anagram group
            self.__grouped_records[map_idx].add(key)

    def anagrams(self):
        """Returns a list of Groups containing anagrams

        Returns:
            list: List of grouped anagrams
        """
        # Populate a new list of all the anagrams 
        new_list = []
        for group in self.__grouped_records:
            if group.count > 1:
                new_list.append(group)

        self.__grouped_records = new_list
                
    def output(self):
        """Generates the final list of anagrams 

        Returns:
            list: list of sublists of anagrams
        """
        anagrams = []
        for group in self.__grouped_records:
            unique_set = set(group.anagrams)
            anagram_list = list(unique_set)
            if len(anagram_list) > 1:
                anagrams.append(anagram_list)
        return anagrams

