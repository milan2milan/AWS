import json
import uuid
import boto3
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