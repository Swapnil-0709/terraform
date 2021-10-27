import json


def lambda_handler(event, context):
    return{
        'StatusCode': 200,
        'body': json.dumos(event['headers']['X-forwarded-For'])
    }