from gcpStorage.utils import list_blobs
from gcpStorage.storage import *
bucket_name = "mr_j_learning_gcp"
list_blobs(bucket_name=bucket_name)

download_blob(bucket_name, 'files names . txt (example)')