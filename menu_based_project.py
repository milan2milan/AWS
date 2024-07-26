import os
from datetime import datetime
import boto3
import os
import json
import uuid
from pymongo import MongoClient
while True:
    option=input("Enter your choice\nEnter 1. for Launch ec2 instance\nEnter 2. for Launch RHEL GUI instance\nEnter 3. for Load any type of file to s3 bucket\nEnter 4. for Connect with mongoDB\nEnter 5. for Send bulk email\nEnter 6. for Audio to text generator\n")
    if (option=="1"):
            #Launch ec2 instance
            a_key=input("Enter your access key: ")
            a_s_key=input("Enter your secret key: ")
            try:
                myec2=boto3.resource("ec2", region_name="ap-south-1", aws_access_key_id=a_key, aws_secret_access_key=a_s_key)
                myec2.create_instances(InstanceType='t2.micro', ImageId='ami-0ec0e125bb6c6e8ec', MaxCount=1, MinCount=1)
            except:
                 print("Please enter right keys!!!")

#------------------------------------------------------------------------------------------------------------------------------
    elif(option=="2"):
            #Launch RHEL GUI instance
            a_key=input("Enter your access key: ")
            a_s_key=input("Enter your secret key: ")
            try:
                myec3=boto3.resource("ec2",region_name="ap-south-1",aws_access_key_id=a_key,aws_secret_access_key=a_s_key)
                myec3.create_instances(InstanceType='t2.micro',ImageId='ami-022ce6f32988af5fa',MaxCount=1,MinCount=1)
            except:
                 print("Please enter right keys!!!")
    elif(option=="3"):
            #load file to s3 bucket
            try:
                a_key=input("Enter your access key: ")
                a_s_key=input("Enter your secret key: ")
                buc=boto3.client('s3', aws_access_key_id=a_key, aws_secret_access_key=a_s_key,region_name="ap-south-1")
                b_name="audio-to-speach-gen"
                file_path=input("Enter your file path")
                from datetime import datetime
                from pathlib import Path
                f_name=Path(file_path).name
                obj_name=str(datetime.now().time().microsecond)+f_name
                buc.upload_file(f_name,b_name,obj_name)
            except:
                 print("Please check your keys or file path!!!")
    elif(option=="4"):  
            #connect with mongoDB
            client=MongoClient(host=os.environ.get("ATLAS_URI"))
            def lambda_handler(event, context):
                try:
                    db=client.MyDB
                    collection=db.MyDB
                    data={"Id":"S01","Name":"Milan Parua"}
                    result=collection.insert_one(data)
        
                    if result.insretd_id:
                        return("Successfuly insert a data")
                    else:
                        return("Sorry,Not inserted")
                except:
                    print("Connection problem!!!")
    elif(option=="5"):
          #send bulk email
          #Must Sender and Recipient email ids are verified by SES service that provided by AWS 
        try:
            s3=boto3.client('s3')
            ses=boto3.client('ses')

            def lambda_handler(event, context):
        
                bucket_name="files-storages"
                file_key=event['Records'][0]['s3']['object']['key']
        
                file_obj=s3.get_object(Bucket=bucket_name,Key=file_key)
                file_data=file_obj['Body'].read().decode('utf-8')
        
        
                email_id=file_data.splitlines()
        
                for email in email_id:
                    send_email(email)    
        
                    return {
                    'statusCode': 200,
                    'body': json.dumps('Hello from Lambda!')
                    }
                def send_email(email):
                    response=ses.send_email(
                    Source='serviceprovider01010@gmail.com',
                    Destination={
                        'ToAddresses': [email]
                    },
                    Message={
                        'Subject':{'Data':'Service from AWS'},
                        'Body':{'Text':{'Data':"Thank you for used our service \n Please use it aga"}}
                    }
                )
        except:
            print("Sorry we can't send email!!!")
    elif(option=="6"):
        #audio to text generator
        try:
            client=boto3.client('transcribe')
            def lambda_handler(event, context):
                genid=uuid.uuid4().int
                file_name=event['Records'][0]['s3']['object']['key']
        
                client.start_transcription_job(TranscriptionJobName='job'+str(genid),
                LanguageCode="en-US",
                MediaFormat="mp3",
                Media={'MediaFileUri': 's3://audio-to-speach-gen/'+file_name},
        
                OutputBucketName="output-store-text"),
                # TODO implement
                return {
                    'statusCode': 200,
                    'body': json.dumps('Hello from Lambda!')
                }
        except:
            print("Some problem occured!!!")
    else:
         print("Please choose valid key")
