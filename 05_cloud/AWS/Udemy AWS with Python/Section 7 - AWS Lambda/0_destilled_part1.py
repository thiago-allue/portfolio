######################
#    Section 7 - AWS Lambda
#
#####################


### ./0a.+S3+List.py ####################################
import json
import boto3  # python sdk and it is available in here you don't need t install

s3 = boto3.resource('s3')

def lambda_handler(event, context):

    s3_buckets = []

    for bucket in s3.buckets.all():
        s3_buckets.append(bucket.name)

    return {
        "statusCode": 200,
        "body": s3_buckets
    }


### ./0b. S3+Upload+Image.py ####################################
import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('s3')

    with open('aws.png', 'rb') as f:
        data = f.read()

    response = client.put_object(
        Bucket="parwizforogh12",
        Body=data,
        Key='aws.png'

    )
    print(response)


### ./1.+creattable.py ####################################
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='Users',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )

    print("Table status:", table.table_status)


### ./2.adddata.py ####################################
import boto3

def lambda_handler(event, context):
    db = boto3.resource('dynamodb')

    table = db.Table('Users')

    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                'id': 1,
                'name': 'parwiz',
                'age': '20'
            }
        )

        batch.put_item(
            Item={
                'id': 2,
                'name': 'john',
                'age': '20'
            }
        )

        batch.put_item(
            Item={
                'id': 3,
                'name': 'abc',
                'age': '37'
            }
        )


### ./3.+getdata.py ####################################
import boto3

def lambda_handler(event, context):
    db = boto3.resource('dynamodb')

    response = db.batch_get_item(
        RequestItems={
            'Users': {
                'Keys': [
                    {
                        'id': 1,

                    },
                    {
                        'id': 2
                    },

                    {
                        'id': 3
                    }
                ]
            }
        }
    )

    print(response['Responses'])


### ./4.+querytab.py ####################################
import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Users')

    resp = table.query(
        KeyConditionExpression=Key('id').eq(1)
    )

    if 'Items' in resp:
        print(resp['Items'][0])


### ./4.+update.py ####################################
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Users')

    table.update_item(
        Key={
            'id': 1,
        },
        UpdateExpression="set age = :g",
        ExpressionAttributeValues={
            ':g': 24
        },
        ReturnValues="UPDATED_NEW"
    )


### ./5.+deleteitem.py ####################################
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Users')

    response = table.delete_item(
        Key={
            'id': 1,
        }
    )
    print(response)