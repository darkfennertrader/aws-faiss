import json
import requests


def lambda_handler(event, context):
    # TODO implementation
    header = {"Content-Type": "application/json"}
    payload = {"message": "Lambda container image invoked!", "event": event}

    return {
        "header": header,
        "statusCode": 200,
        "body": json.dumps(payload),
    }
