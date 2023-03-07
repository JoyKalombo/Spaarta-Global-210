from google.cloud import storage

def list_blobs(bucket_name):
    """Lists all of the buckets"""

    # bucket_name = "your-bucket-name"
    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.

    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)