# Lambda and DynamoDB workshop

## Getting started
Log in to your AWS account and navigate to Lambda. Create a new function with "Use a blueprint":
* **Blueprint name:** Python version of "Create a microservice that interacts with a DDB table"
* **Function name:** `weatherLookup`
* **Execution role:** Create a new role with basic Lambda permissions
* **Lambda function code:** Replace with the contents of function01.py in this repo
* **API Gateway trigger > Intent:** Create a new API
* **API type:** HTTP API

Once you're in the function editor, click the API Gateway box in the Function overview section. This will display the API endpoint URL for your function. Open this in a new tab and verify that you see "Hello, World!". If so, your Lambda function is working!

## Simple Lambda functions
### Version 01
[function01.py](function01.py) has a simple "Hello, World!" response and takes no input.

### Version 02
[function02.py](function02.py) receives a URL query parameter called `zip` and echoes it back in the response. Add this to your testing URL to try it: `?zip=78758`.

### Version 03
[function03.py](function03.py) ignores (for now) the `zip` parameter and hardcodes a latitude/longitude. Then it uses that to call an open-source weather API ([Open-Meteo](https://open-meteo.com/)) to get the forecast high temperature for today at that location.

## Expanding to use DynamoDB
Before we continue, we need to set up a DynamoDB table and give our Lambda function access to it.

Go to DynamoDB in your AWS Console and click Create table:
* **Table name:** `zipCodeToLatLong`
* **Partition key:** `zipCode`
* **Table settings:** Default settings

Now open up the table and click Explore table items. Click Create item and set zipCode to `78758`. Then click Add new attribute, select number, and set the attribute name to `latitude` with a value of `30.2672`. Add another number attribute with name `longitude` and value `-97.7431`. Click Create item to save it.

Now go back to Lambda and open up your `weatherLookup` function so we can use this data there.

## Version 04
[function04.py](function04.py) uses the `zip` parameter to look up the latitude/longitude in the DynamoDB table and pass that to the Open-Meteo API.

If you get the following error, you need to grant access to the Lambda function to access DynamoDB:

```
An error occurred (AccessDeniedException) when calling the GetItem operation: User: arn:aws:sts::000000000000:assumed-role/weatherLookup-role-ryvomkio/weatherLookup is not authorized to perform: dynamodb:GetItem on resource: arn:aws:dynamodb:us-east-2:000000000000:table/zipCodeToLatLong because no identity-based policy allows the dynamodb:GetItem action
```

In the function editor, click the Configuration tab and select Permissions. Click the link under Role name to open the role in a new tab. There, under the Permissions > Permission policies section, click Add permissions > Attach policies. Search for "dynamo", check the box next to `AmazonDynamoDBFullAccess`, and click Add permissions.