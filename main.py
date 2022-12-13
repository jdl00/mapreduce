# Local imports
from build_stop_words import build_json
from book_anagrams import BookAnagrams

# External imports
from flask import Flask
from time import perf_counter
import os

app = Flask(__name__)

@app.route("/")
def run():
    start = perf_counter()
    build_json()
    anagrams = BookAnagrams()
    anagrams.run()
    return f'Succesfully ran in {perf_counter() - start:.3f} seconds'


def main():
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
if __name__ == "__main__":
    main()
