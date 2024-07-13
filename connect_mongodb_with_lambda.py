import json
import os
from pymongo import MongoClient
client=MongoClient(host=os.environ.get("ATLAS_URI"))

def lambda_handler(event, context):
    db=client.MyDB
    collection=db.MyDB
    data={"Id":"S01","Name":"Milan Parua"}
    result=collection.insert_one(data)
    
    if result.insretd_id:
        return("Successfuly insert a data")
    else:
        return("Sorry,Not inserted")
