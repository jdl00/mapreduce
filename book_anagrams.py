# Local imports
from mapper import Mapper
from shuffler import Shuffler
from reducer import Reducer

#External Includes
from time import perf_counter
from multiprocessing import cpu_count
from google.cloud import storage
from uuid import uuid1
from datetime import datetime
from google.oauth2.service_account import Credentials

class BookAnagrams():
    """Holds the main logic for input/output of buckets
       and runs the MapReduce programming model. 
    """

    # Input bucket name 
    CONST_INPUT_BUCKET = "word_input"
    # Input file name
    CONST_INPUT_FILE_NAME = "books.txt"
    # Project used
    CONST_PROJECT = "cloudcoursework-370915"
    # Output bucket name
    CONST_OUTPUT_BUCKET = "word_output"

    def __init__(self):
        """Creates a BookAnagrams instance
        """
        self.__cores = cpu_count()
        self.__input_data = ""
        self.__list_data = []
        self.__split_data = []
        self.__output_data = []
        self.__credentials = Credentials.from_service_account_file("key.json")
        self.__file_name = ""

    def __download_data(self):
        """Downloads the initial book text file to memory
        """
        storage_client = storage.Client(project=self.CONST_PROJECT,
                                        credentials=self.__credentials)

        bucket = storage_client.get_bucket(self.CONST_INPUT_BUCKET)
        document = bucket.blob(self.CONST_INPUT_FILE_NAME)

        self.__input_data = document.download_as_string().decode('utf-8').split('\n')

    def __form_output_string(self):
        """Forms the output by creating a string format and adding a new line

        Returns:
            string: Formatted anagrams
        """
        string_anagrams = [f'{", ".join(anagrams)}\n' for anagrams in self.__output_data]
        return ''.join(string_anagrams)


    def __output(self):
        """Outputs the file to the bucket, and formats.
        """

        # Generate a unique ID 
        unique_id = uuid1()

        # Get the current date and time
        now = datetime.now()
        date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")

        # Combine the unique ID and the date/time string to create the final ID
        self.__file_name = f"{unique_id}_{date_time_string}"

        # Create a client object to the output bucket 
        storage_client = storage.Client(project=self.CONST_PROJECT,
                                        credentials=self.__credentials)
        bucket = storage_client.bucket(self.CONST_OUTPUT_BUCKET)
        # Create the file name for the output results
        file = bucket.blob(f'{self.__file_name}.txt')

        # Form the final output string
        output_string = self.__form_output_string()

        # Upload the output
        file.upload_from_string(output_string)
        print(f'Wrote anagrams to file {self.__file_name}.txt')

    def __split(self):
        """Splits the data into roughly equal sections based on the amount of cores

        Returns:
            list: list of sublists of split data
        """
        return [self.__input_data[i::self.__cores] for i in range(self.__cores)]

    def __run_mapper(self):
        """Runs the mapper.
        """

        self.__split_data = self.__split()
        start = perf_counter()

        map_data = []
        for data in self.__split_data:
            # Map the blocks of data
            mapper = Mapper(data)
            mapper.map()
            map_data.append(mapper.get())
        
        end = perf_counter()
        print(f"Mapper: Elapsed time: {end-start:.3f} seconds")

        # Join the chunks back into one
        self.__list_data = []
        for sublist in map_data:
            self.__list_data.extend(sublist)

    def __run_shuffler(self):
        """Runs the shuffler.
        """
        start = perf_counter()
        
        #Run the shuffler
        shuffler = Shuffler(self.__list_data)
        shuffler.shuffle()
        self.__list_data = shuffler.get()

        end = perf_counter()
        print(f"Shuffler: Elapsed time: {end-start:.3f} seconds")
                
    def __run_reducer(self):
        """Runs the reducer.
        """
        start = perf_counter()

        # Run the reducer
        reducer = Reducer(self.__list_data)
        reducer.reduce()
        reducer.anagrams()
        self.__output_data = reducer.output()

        end = perf_counter()
        print(f"Reducer: Elapsed time: {end-start:.3f} seconds")

    def run(self):
        """Runs the main program logic.
        """
        print("Downloading book data from bucket.")
        self.__download_data()
        
        print("Mapping data.")
        self.__run_mapper()

        print("Shuffling data.")
        self.__run_shuffler()

        print("Reducing data.")
        self.__run_reducer()

        print(f'Writing angrams to bucket: word_output')
        self.__output()


