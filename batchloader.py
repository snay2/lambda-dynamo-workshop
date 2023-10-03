import boto3

dynamo_table = boto3.resource('dynamodb').Table('zipCodeToLatLong')

mappings = [
    {
        'zipCode': 90210,
        'latitude': 34.07,
        'longitude': -118.40,
    },
    {
        'zipCode': 10001,
        'latitude': 40.71,
        'longitude': -74.01,
    },
    {
        'zipCode': 94111,
        'latitude': 37.77,
        'longitude': -122.42,
    },
    {
        'zipCode': 22202,
        'latitude': 38.88,
        'longitude': -77.10,
    },
    {
        'zipCode': 30354,
        'latitude': 33.75,
        'longitude': -84.39,
    },
    {
        'zipCode': 60606,
        'latitude': 41.85,
        'longitude': -87.65,
    },
]

def lambda_handler(event, context):
    for mapping in mappings:
        dynamo_table.put_item(Item={
            # We need str() because the DynamoDB attribute types are string
            'zipCode': str(mapping['zipCode']),
            'latitude': str(mapping['latitude']),
            'longitude': str(mapping['longitude']),
        })
