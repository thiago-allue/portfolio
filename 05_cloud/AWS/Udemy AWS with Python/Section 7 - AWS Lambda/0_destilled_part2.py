######################
#    Section 7 - AWS Lambda
#
#####################

### ./1.+CreateRule.py ####################################
import boto3
import json

iam = boto3.client('iam')

role_policy = {

    "Version":"2012-10-17",
    "Statement":[
        {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{
                "Service":"lambda.amazonaws.com"
            },
            "Action":"sts:AssumeRole"
        }

    ]

}
response = iam.create_role(
    RoleName='PyLambdaBasicExecution',
    AssumeRolePolicyDocument=json.dumps(role_policy)
)

print(response)


### ./2.+CreateLambdaFunction.py ####################################
import boto3

iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')

with open('lambda.zip', 'rb') as f:
    zipped_code = f.read()

role = iam_client.get_role(RoleName='PyLambdaBasicExecution')

response = lambda_client.create_function(
    FunctionName='helloWorldLambda',
    Runtime='python3.9',
    Role=role['Role']['Arn'],
    Handler='lambda_function.lambda_handler',
    Code=dict(ZipFile=zipped_code),
    Timeout=300,

)

print(response)


### ./3.+InvokeLambda.py ####################################
import json
import boto3

lambda_client = boto3.client('lambda')

test_event = dict()

response = lambda_client.invoke(
    FunctionName='helloWorldLambda',
    Payload = json.dumps(test_event)
)

print(response['Payload'])
print(response['Payload'].read().decode('utf-8'))


### ./4.+DescribeLambda.py ####################################
import boto3
from pprint import pprint

lambda_client = boto3.client('lambda')

response = lambda_client.get_function(
    FunctionName='helloWorldLambda'
)
pprint(response)


### ./5.+DeleteLambda.py ####################################
import boto3

lambda_client = boto3.client('lambda')

response = lambda_client.delete_function(
    FunctionName='helloWorldLambda'
)

print(response)
