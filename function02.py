import json

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    zip_code = event['queryStringParameters']['zip']
    response = 'The ZIP code you provided is ' + zip_code
    return respond(None, response)
