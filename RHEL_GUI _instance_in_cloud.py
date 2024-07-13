import boto3
myec3=boto3.resource("ec2",region_name="ap-south-1",aws_access_key_id="Enter your access key",aws_secret_access_key="Enter your screte access key")
myec3.create_instances(InstanceType='t2.micro',ImageId='ami-022ce6f32988af5fa',MaxCount=1,MinCount=1)

#Download Key ex:mykey.pem
#Open terminal on the same directory where present your key "mykey.pem"
#using ssh login on RHEL
#Then Enjoy it from your Local Machine