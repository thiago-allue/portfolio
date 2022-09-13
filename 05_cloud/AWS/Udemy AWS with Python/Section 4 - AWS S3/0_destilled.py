######################
#    Section 4 - AWS Simple Storage Service (S3)
#
#####################


### ./1.+CreateBucket.py ####################################
import boto3

bucket = boto3.resource('s3')

response = bucket.create_bucket(
    Bucket = "parwizforogh7777",
    ACL="private",
)

print(response)


### ./2.+ClientBucket.py ##################################
import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket = "parwizforogh12",
    ACL = "private",

)

print(response)


### ./3.+UploadingImage.py ##################################
import boto3

client = boto3.client('s3')

with open('aws.png', 'rb') as f:
    data = f.read()

response = client.put_object(
    ACL="public-read-write",
    Bucket = "parwizforogh12",
    Body=data,
    Key='aws.png'
)

print(response)


### ./4.+ListingBuckets.py ##################################
import boto3

'''
bucket = boto3.client('s3')

response = bucket.list_buckets()

print("Listing all buckets")

for bucket in response['Buckets']:
    print(bucket['Name'])

'''

resource = boto3.resource('s3')

iterator = resource.buckets.all()

print("Listing all buckets")

for bucket in iterator:
    print(bucket.name)


### ./5.+DeleteBucket.py ##################################
import boto3

'''
client = boto3.client('s3')

bucket_name = "parwizforogh7777"

client.delete_bucket(Bucket=bucket_name)

print("S3 Bucket has been deleted")

'''

#Delete bucket with aws resource

resource = boto3.resource('s3')

bucket_name = "parwizforogh7777"

s3_bucket =resource.Bucket(bucket_name)

s3_bucket.delete()

print(" This {} bucket has been deleted  ".format(s3_bucket))


### ./6.+DeleteNonEmpy.py ##################################
import boto3

BUCKET_NAME = "parwizforogh7777"

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

def clean_up():
    #delete the object
    for s3_object in s3_bucket.objects.all():
        s3_object.delete()

    #delete bucket versioning
    for s3_object_ver in s3_bucket.object_versions.all():
        s3_object_ver.delete()

    print("S3 bucket cleaned")

clean_up()

s3_bucket.delete()

print("The bucket has been deleted")


### ./7.+UploadFile.py ##################################
import boto3

BUCKET_NAME =   "parwizforogh12"

s3_client = boto3.client('s3')

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print("{} has been uploaded to {} bucket".format(file_name, BUCKET_NAME))

upload_files("file.txt", BUCKET_NAME)

'''
# uploading with resource

BUCKET_NAME =   "parwizforogh7777"

s3_client = boto3.resource('s3')

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.meta.client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print("{} has been uploaded to {} bucket".format(file_name, BUCKET_NAME))

upload_files("myfile.txt", BUCKET_NAME)

'''


### ./8.+DownloadFile.py ##################################
import boto3

BUCKET_NAME = "parwizforogh12"

s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(BUCKET_NAME, 'file.pdf')

s3_object.download_file('downloaded.pdf')

print("File has been downloaded")


### ./9.+GetName.py ##################################

import boto3

BUCKET_NAME = "parwizforogh22"

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print("Listing Bucket Files or Objects")

for obj in s3_bucket.objects.all():
    print(obj.key)


### ./10.+ListingFilter.py  ####################################
import boto3

BUCKET_NAME = "parwizforogh7777"

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print("Listing Filtered File")

for obj in s3_bucket.objects.filter(Prefix="file"):
    print(obj.key)

### ./11.+GetSummary.py ####################################
import boto3

s3 = boto3.resource('s3')

object_summary = s3.ObjectSummary("parwizforogh7777", "file.pdf")

print(object_summary.bucket_name)
print(object_summary.key)

### ./12.+CopyObject.py ####################################

import boto3

s3 = boto3.resource('s3')

copy_source = {
    'Bucket': 'parwizforogh7777',
    'Key': 'file.pdf'
}

s3.meta.client.copy(copy_source, 'parwizforogh12', 'copied.pdf')

### ./13.+DeleteObjects.py ####################################
import boto3

client = boto3.resource('s3')

'''
response = client.delete_object(
    Bucket = 'parwizforogh7777',
    Key='file.pdf'
)

print(response)

'''

# delete multiple files or objects

response = client.delete_objects(
    Bucket='parwizforogh7777',
    Delete={
        'Objects': [
            {
                'Key': 'file.txt'
            },

            {
                'Key': 'myfile.txt'
            }

        ]
    }
)

print(response)

### ./14.+GetWebsiteConfig.py ##################################
import boto3
from pprint import pprint

client = boto3.client('s3')

response = client.get_bucket_website(
    Bucket="awstutorial12"
)

pprint(response)

### ./15.+DeletePloicy.py##################################
import boto3

client = boto3.client('s3')

response = client.delete_bucket_policy(
    Bucket="awstutorial12"
)

print(response)

### ./16.+DeleteWebsite.py##################################
import boto3

client = boto3.client('s3')

response = client.delete_bucket_website(
    Bucket="awstutorial12"
)

print(response)
