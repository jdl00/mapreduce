from mapper import Mapper
from shuffler import Shuffler
from reducer import Reducer



words = None
with open("test_book.txt", 'r') as f:
    words = f.readlines()
mapper = Mapper(words)
mapper.map()
map = mapper.get()

shuffler = Shuffler(map)
shuffler.shuffle()
shuffled_mapping = shuffler.get_shuffled_mapping()

reducer = Reducer(shuffled_mapping)
reducer.reduce()
reducer.output()