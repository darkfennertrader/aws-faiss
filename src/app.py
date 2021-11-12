import json
import boto3
import requests
import memcache
from sentence_transformers import SentenceTransformer
from config import Config


dynamodb = boto3.resource("dynamodb", region_name=Config.REGION)
cache_faiss = memcache.Client([Config.MEMCACHE_ADDRESS], debug=0)

sentences = ["This is an example sentence", "Each sentence is converted"]


def lambda_handler(event, context):
    # TODO implementation
    header = {"Content-Type": "application/json"}
    payload = {"message": "Lambda container image invoked!", "event": event}

    return {
        "header": header,
        "statusCode": 200,
        "body": json.dumps(payload),
    }
