import boto3
buc=boto3.client('s3', aws_access_key_id="your access key", aws_secret_access_key="your secret access key",region_name="ap-south-1")
b_name="audio-to-speach-gen"
file_path=input("Enter your file path")
from datetime import datetime
from pathlib import Path
f_name=Path(file_path).name
obj_name=str(datetime.now().time().microsecond)+f_name
print(obj_name)
buc.upload_file(f_name,b_name,obj_name)