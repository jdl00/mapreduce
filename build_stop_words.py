from requests import get
from json import dump

'''
Simple script to build the stop words json file
'''
def build_json():
    # Get the list of stop words from the url
    stop_words = ""
    with get("https://www.textfixer.com/tutorials/common-english-words-with-contractions.txt") as response:
        if response.status_code != 200:
            assert False, "Failed to get stop words"
        stop_words = response.text

    # Split these words using the comma to form a new list
    split_words = stop_words.split(",")
    with open("stop_words.json", "w") as json_file:
        dump(split_words, json_file)
