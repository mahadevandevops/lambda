import json
import random
import time
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

def handler(event, context):
    xray_recorder.put_annotation("api", "orders")
    
    # Simulate some processing
    time.sleep(0.2)
    
    # Simulate random error (will help you test rollback)
    if event.get("fail") == True:
        raise Exception("Simulated error for canary rollback")
    
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Order processed successfully",
            "trace_id": xray_recorder.get_trace_entity().trace_id
        })
    }
    return response
