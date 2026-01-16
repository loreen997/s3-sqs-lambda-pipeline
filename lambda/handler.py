import json

def lambda_handler(event, context):
    for record in event["Records"]:
        print("SQS record body:", record["body"])
    return {"ok": True}
