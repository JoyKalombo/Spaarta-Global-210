import os
from google.cloud import storage



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/jk/PycharmProjects/pythonProject1/Spaarta-Global-210' \
                                               '/Data_Engineering/cloudProjects/private_key_for_GCP_project.json'

# initialize the client object
client = storage.Client()

bucket_name =
bucket =

buckets = client.list_buckets()

for bucket in buckets:
    print(bucket.name)

def read_file(blob_name):
    blob = bucket.blob(blob_name)
    data_string = blob.download_as_string()
    print(data_string.decode())

def download_file(blob_name):
    blob = bucket.blob(blob_name)
    blob.download_to_filename(blob_name)
    print("Download from bucket {} to local file {}.".format(bucket_name, blob_name))

def upload_file(blob_name):
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(blob_name)
    print("Upload from local file {} to bucket {}.".format(bucket_name, blob_name))