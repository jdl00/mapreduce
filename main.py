# Local imports
from build_stop_words import build_json
from book_anagrams import BookAnagrams

def main():

    build_json()
    anagrams = BookAnagrams()
    anagrams.run()

if __name__ == "__main__":
    main()

'''
start = perf_counter()
# Run the mapper
mapper = Mapper(words)
mapper.map()
map = mapper.get()
end = perf_counter()
print(f"Mapper: Elapsed time: {end-start:.3f} seconds")

# Run the shuffler
start = perf_counter()
shuffler = Shuffler(map)
shuffler.shuffle()
shuffled_mapping = shuffler.get_shuffled_mapping()
end = perf_counter()
print(f"Shuffler: Elapsed time: {end-start:.3f} seconds")

# Run the reducer
start = perf_counter()
reducer = Reducer(shuffled_mapping)
reducer.reduce()
reducer.anagrams()
end = perf_counter()
print(f"Shuffler: Elapsed time: {end-start:.3f} seconds")
reducer.output()

def main():
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("coc105-gutenberg-5000books")

    for blob in bucket.list_blobs():
        print(blob.name)
    


if __name__ == "__main__":
    main()

'''
