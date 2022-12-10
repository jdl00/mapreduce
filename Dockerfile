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

# In order to launch our python code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter 'main.py' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# Here we put the file at the image root folder.


# Install gsutil
RUN curl https://sdk.cloud.google.com | bash
ENV PATH /root/google-cloud-sdk/bin:$PATH
RUN gcloud components install gsutil

# Run the gsutil command when the container starts
CMD ["gsutil"]

COPY main.py /
COPY group.py /
COPY build_stop_words.py /
COPY mapper.py /
COPY reducer.py /
COPY shuffler.py /

# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following command will execute "python ./main.py".
CMD [ "python", "./main.py" ]
