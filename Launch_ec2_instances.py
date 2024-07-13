import boto3
myec2=boto3.resource("ec2", region_name="ap-south-1", aws_access_key_id="add your access key", aws_secret_access_key="add your secret key")
myec2.create_instances(InstanceType='t2.micro', ImageId='ami-0ec0e125bb6c6e8ec', MaxCount=1, MinCount=1)