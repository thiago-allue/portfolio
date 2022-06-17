######################
#    Section 2 - AWS and IAM Introduction
#       IAM - Identity and Access Management
#####################



### 1.CREATE A USER ####################
import boto3

def create_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)

create_user('testuser2')


### ./2.+ListAllUsers.py  ########################
def all_users():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            Arn = user['Arn']
            print('Username : {} Arn : {}'.format(username, Arn))

all_users()


### ./3.+UpdateUser.py  ########################
def update_user(old_username, new_username):
    iam = boto3.client('iam')

    response = iam.update_user(
        UserName=old_username,
        NewUserName=new_username
    )

    print(response)

update_user('testuser2', 'testuser')


### /4.+CreatePolicy.py  ########################
import json


def create_policy():
    iam = boto3.client('iam')

    user_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName='pyFullAccess',
        PolicyDocument=json.dumps(user_policy)
    )

    print(response)


create_policy()


### ./5.+ListAllPolicy.py  ########################
def list_policies():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="AWS"):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            Arn = policy['Arn']

            print('Policy Name : {} Arn : {}'.format(policy_name, Arn))

list_policies()


### ./6.+AttachPolicyUser.py  ########################
def attach_policy(policy_arn, username):
    iam = boto3.client('iam')

    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)

attach_policy('arn:aws:iam::aws:policy/AmazonRDSFullAccess', 'testuser')


### ./7.+DetachUser.py  ########################
iam = boto3.client('iam')

response = iam.detach_user_policy(
    UserName='testupdated',
    PolicyArn='arn:aws:iam::651366224884:policy/pyFullAccess'
)

print(response)


### ./8.+CreateGroup.py  ########################
def create_group(group_name):
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)


create_group('S3Admins')


### 10. ADD USER ########################
def add_user(username, group_name):
    iam = boto3.client('iam')
    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )
    print(response)

add_user('s3user', 'S3Admins')


### 11. DETACH GROUP ########################
def detach_group(user_group, arn):
    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName=user_group,
        PolicyArn=arn
    )
    print(response)

detach_group('RDSAdmins', 'arn:aws:iam::aws:policy/AmazonRDSFullAccess')


### ./12.+CreateAccess.py  ########################
'''
def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)

create_access('testuser')

'''

def update_access():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId='AKIAZPKDT2P2K2ESBO4H',
        Status='Inactive',
        UserName='testuser'
    )

update_access()


### ./13.+CreateLogin.py  ########################
def create_login(username):
    iam = boto3.client('iam')

    login_profile = iam.create_login_profile(
        Password='Mypassword@1',
        PasswordResetRequired=False,
        UserName=username
    )
    print(login_profile)

create_login('test')


### ./14.+DeleteUser.py  ########################
def delete_myuser(username):
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName=username
    )
    print(response)

delete_myuser('test')


### ./15.+DeleteUserFromGroup.py  ########################
def delete_user_group(username, groupName):
    iam = boto3.resource('iam')

    group = iam.Group(groupName)

    response = group.remove_user(
        UserName=username
    )
    print(response)

delete_user_group('s3user', 'S3Admins')