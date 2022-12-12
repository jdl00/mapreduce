# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM python:latest

# Install pip
RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get -y install curl
RUN apt-get -y install gcc
RUN pip3 install requests
RUN pip3 install google-cloud-storage

COPY main.py /
COPY group.py /
COPY build_stop_words.py /
COPY mapper.py /
COPY reducer.py /
COPY shuffler.py /
COPY book_anagrams.py /
COPY key.json /

# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following command will execute "python ./main.py".
CMD [ "python", "./main.py" ]
