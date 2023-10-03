import json
import urllib

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
    latitude = 30.2672
    longitude = -97.7431

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': 'temperature_2m_max',
        'temperature_unit': 'fahrenheit',
        'timezone': 'America/Chicago',
        'forecast_days': 1,
    }
    
    base_url = 'https://api.open-meteo.com/v1/forecast'
    params = urllib.parse.urlencode(params)
    res = urllib.request.urlopen(urllib.request.Request(
        url=base_url + '?' + params,
        method='GET'))
    response = json.loads(res.read())
    temp = response['daily']['temperature_2m_max'][0]
    return respond(None, temp)
