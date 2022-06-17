######################
#    Section 3 - AWS and DynamoDB
#       Part 1
#####################

### ./1.+PutData.py ##################################
import boto3

db = boto3.resource('dynamodb')
table = db.Table('employee')

table.put_item(
    Item = {
        'emp_id':"1",
        'name':"Parwiz",
        'age':28
    }
)


### ./2.+ClientPut.py ##################################
import boto3

db = boto3.client('dynamodb')

response = db.put_item(
    TableName='employee',

    Item = {
        'emp_id': {
            'S':'4'
        },
        'name':{
            'S':'John'
        },

        'age': {
            'S':'25'
        }
    }
)


### ./3.+BatchWrite.py ##################################
db = boto3.resource('dynamodb')

table = db.Table('employee')

with table.batch_writer() as batch:
    batch.put_item(
        Item = {
            'emp_id':'5',
            'name':'anothername',
            'age':'35'
        }
    )

    batch.put_item(
        Item = {
            'emp_id':'6',
            'name':'abc',
            'age':'32'
        }
    )

    batch.put_item(
        Item={
            'emp_id': '7',
            'name': 'abc7',
            'age': '37'
        }
    )


### ./4.+GetData.py ##################################
from pprint import pprint

db = boto3.client('dynamodb')

response = db.describe_table(
    TableName = 'employee'
)
pprint(response)


###  ./5.+ListTables.py ##################################
import boto3

db = boto3.client('dynamodb')

response = db.list_tables()

print(response['TableNames'])


### ./6.+ChangeTable.py ##################################
import boto3

db = boto3.client('dynamodb')

response = db.update_table(
    TableName='employee',
    BillingMode='PROVISIONED',

    ProvisionedThroughput={
        'ReadCapacityUnits':1,
        'WriteCapacityUnits':1
    }
)

print(response)


###./7.+CreateBackcup.py ##################################
import boto3

db = boto3.client('dynamodb')


'''
response = db.create_backup(
    TableName='employee',
    BackupName='ArticleBackUp'
)

print(response)

'''


response = db.delete_backup(
    BackupArn='arn:aws:dynamodb:us-east-1:651366224884:table/employee/backup/01644585631214-8e886bd4'

)

print(response)


### ./7b.GetItem.py ##################################
import boto3

db = boto3.resource('dynamodb')

table = db.Table('employee')

response = table.get_item(
    Key = {
        'emp_id':"5"
    }
)

print(response['Item'])

### ./8.+GetBatch.py ##################################
import boto3
from pprint import pprint

db = boto3.resource('dynamodb')

response = db.batch_get_item(
    RequestItems={
        'employee':{
            'Keys':[
                {
                    'emp_id':'1',

                },
                {
                    'emp_id':'2'
                },

                {
                    'emp_id':'3'
                },

                {
                    'emp_id':'4'
                }
            ]
        }
    }
)

pprint(response['Responses'])


### ./9.+GetItemClient.py ##################################
import boto3

db = boto3.client('dynamodb')

response = db.get_item(
    TableName='employee',
    Key={
        'emp_id':{
            'S':'2'
        }
    }
)

print(response['Item'])

### ./10.+ScanData.py  ##################################
import boto3
from pprint import pprint

db = boto3.resource('dynamodb')

table = db.Table('employee')

response = table.scan()

data = response['Items']
pprint(data)