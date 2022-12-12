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

    def __init__(self):
        self.__cores = cpu_count()
        self.__input_data = ""
        self.__list_data = []
        self.__output_bucket = None
        self.__split_data = []
        self.__output_data = []
        self.__credentials = Credentials.from_service_account_file("key.json")



    def __download_data(self):
        storage_client = storage.Client(project="cloudcoursework-370915",
                                        credentials=self.__credentials)
        bucket = storage_client.get_bucket("word_input")
        document = bucket.blob("8956.txt")
        self.__input_data = document.download_as_string().decode('utf-8').split('\n')

    def __form_output_string(self):
        string_anagrams = [f'{", ".join(anagrams)}\n' for anagrams in self.__output_data]
        return ''.join(string_anagrams)


    def __output(self):
        # Generate a unique ID using the uuid1() function
        unique_id = uuid1()

        # Get the current date and time
        now = datetime.now()

        # Convert the date and time to a string using strftime()
        date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")

        # Combine the unique ID and the date/time string to create the final ID
        final_id = f"{unique_id}_{date_time_string}"
        
        storage_client = storage.Client(project="cloudcoursework-370915",
                                        credentials=self.__credentials)
        bucket = storage_client.bucket("word_output")
        file = bucket.blob(f'{final_id}.txt')

        output_string = self.__form_output_string()

        # Write the string to the file
        file.upload_from_string(output_string)

    def __split(self):
        return [self.__input_data[i::self.__cores] for i in range(self.__cores)]

    def __run_mapper(self):

        self.__split_data = self.__split()
        start = perf_counter()

        map_data = []
        for data in self.__split_data:
            mapper = Mapper(data)
            mapper.map()
            map_data.append(mapper.get())
        
        end = perf_counter()
        print(f"Mapper: Elapsed time: {end-start:.3f} seconds")
        self.__list_data = []
        for sublist in map_data:
            self.__list_data.extend(sublist)

    def __run_shuffler(self):
        # Run the shuffler
        start = perf_counter()
        data = []
        shuffler = Shuffler(self.__list_data)
        shuffler.shuffle()
        self.__list_data = shuffler.get_shuffled_mapping()
        end = perf_counter()
        print(f"Shuffler: Elapsed time: {end-start:.3f} seconds")
                
    def __run_reducer(self):
        # Run the shuffler
        start = perf_counter()
        reducer = Reducer(self.__list_data)
        reducer.reduce()
        reducer.anagrams()
        self.__output_data = reducer.output()
        end = perf_counter()
        print(f"Reducer: Elapsed time: {end-start:.3f} seconds")
        #[print(words) for words in self.__output_data]

    def run(self):
        print("Downloading book data from bucket.")
        self.__download_data()
        
        print("Mapping data.")
        self.__run_mapper()

        print("Shuffling data.")
        self.__run_shuffler()

        print("Reducing data.")
        self.__run_reducer()

        print(f'Writing angrams to bucket {self.__output_bucket}')
        self.__output()


