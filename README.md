# MapReduce implementation to find anagrams of books

## Aims:
- Should be a serverless approach
- The code should be robust and able to withstand change
- The code should be able to scale with ease
## Building:
- You must also download your auth key and set the name as key.json
- cloud auth configure-docker
- docker build -t gcr.io/project/container-name . --platform linux/amd64 (e.g gcr.io/cloudcoursework-370915/map-reduce-book-anagrams)
- docker push gcr.io/cloudcoursework-370915/map-reduce-book-anagrams-2
-  gcloud beta run jobs create mapreduce --image gcr.io/cloudcoursework-370915/map-reduce-book-anagrams --execute-now
- The cloud run, can be reran by using gcloud beta run jobs execute mapreduce
## Running: 
- The application is currently hosted on https://mapreduce-7cjhgzyl7q-ew.a.run.app
- The application can simply be run by performing curl on the address
## Buckets:
- The input bucket is gs://coc150-jdl-2022-book-anagram-word-input 
- The output bucket is gs://
 gs://coc150-jdl-2022-book-anagram-word-output