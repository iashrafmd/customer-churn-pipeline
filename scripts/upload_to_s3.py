import boto3
import os

s3 = boto3.client("s3")

bucket_name = os.getenv("S3_BUCKET")
local_folder = "/opt/airflow/data/raw"

for file_name in os.listdir(local_folder):
    file_path = os.path.join(local_folder, file_name)
    s3_key = f"raw/{file_name}"

    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"Uploaded {file_name} to S3")
    