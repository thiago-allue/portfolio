#    Section 7 - AWS Lambda
#
#####################

### ./1.+CreateStack.py ####################################
import boto3

cf_client = boto3.client('cloudformation')
#cf_resource = boto3.resource('cloudformation')

with open('Dynamodb.yml', 'r') as f:
    dy_template = f.read()
    #print(dy_template)

params = [
    {
        'ParameterKey': 'HashKeyElementName',
        'ParameterValue':'EmployeeId'
    }
]

response = cf_client.create_stack(
    StackName='dynamostack',
    TemplateBody=dy_template,
    Parameters=params
)
print(response)


### ./2.+DescribeStack.py ####################################
import boto3

cf_client = boto3.client('cloudformation')

response = cf_client.describe_stacks(
    StackName='dynamostack'
)

print(response)


### ./3.+GetTemplate.py ####################################
import boto3
from pprint import pprint

cf_client = boto3.client('cloudformation')

response = cf_client.get_template(
    StackName='dynamostack'
)

#pprint(response)
pprint(response['TemplateBody'])


### ./4.+DeleteStack.py ####################################
import boto3

cf_client = boto3.client('cloudformation')

response = cf_client.delete_stack(
    StackName='dynamostack'
)

print(response)
