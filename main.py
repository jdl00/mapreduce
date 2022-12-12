# Local imports
from build_stop_words import build_json
from book_anagrams import BookAnagrams

def main():

    build_json()
    anagrams = BookAnagrams()
    anagrams.run()

if __name__ == "__main__":
    main()