from mapper import Mapper
from shuffler import Shuffler
from reducer import Reducer

words = None
with open("test_book.txt", 'r') as f:
    words = f.readlines()

# Run the mapper
mapper = Mapper(words)
mapper.map()
map = mapper.get()


# Run the shuffler
shuffler = Shuffler(map)
shuffler.shuffle()
shuffled_mapping = shuffler.get_shuffled_mapping()

# Run the reducer
reducer = Reducer(shuffled_mapping)
reducer.reduce()
reducer.output()