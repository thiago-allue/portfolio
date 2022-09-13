######################
#    Section 3 - AWS and DynamoDB
#
#####################

### ./1.+CreateTable.py #####################################
import boto3

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName':'year',
                'KeyType':'HASH'
            },

            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'
            }
        ],

        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits':10,
            'WriteCapacityUnits':10
        }


    )

    return table


if __name__ == "__main__":
    movie_table = create_movie_table()
    print("Table status : ", movie_table.table_status)


###./2.+LoadMovie.py #####################################
import boto3
import json
from decimal import Decimal

def load_movie(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie : ", year, title)
        table.put_item(Item=movie)

if __name__=="__main__":
    with open('moviedata.json') as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)

    load_movie(movie_list)


### 2. moviedata.json #####################################
[

    {
        "year": 2013,
        "title": "Rush",
        "info": {
            "directors": ["Ron Howard"],
            "release_date": "2013-09-02T00:00:00Z",
            "rating": 8.3,
            "genres": [
                "Action",
                "Biography",
                "Drama",
                "Sport"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQyMDE0MTY0OV5BMl5BanBnXkFtZTcwMjI2OTI0OQ@@._V1_SX400_.jpg",
            "plot": "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.",
            "rank": 2,
            "running_time_secs": 7380,
            "actors": [
                "Daniel Bruhl",
                "Chris Hemsworth",
                "Olivia Wilde"
            ]
        }
    },
    {
        "year": 2013,
        "title": "Prisoners",
        "info": {
            "directors": ["Denis Villeneuve"],
            "release_date": "2013-08-30T00:00:00Z",
            "rating": 8.2,
            "genres": [
                "Crime",
                "Drama",
                "Thriller"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTg0NTIzMjQ1NV5BMl5BanBnXkFtZTcwNDc3MzM5OQ@@._V1_SX400_.jpg",
            "plot": "When Keller Dover's daughter and her friend go missing, he takes matters into his own hands as the police pursue multiple leads and the pressure mounts. But just how far will this desperate father go to protect his family?",
            "rank": 3,
            "running_time_secs": 9180,
            "actors": [
                "Hugh Jackman",
                "Jake Gyllenhaal",
                "Viola Davis"
            ]
        }
    },
(..)


### ./3.+GetData.py #####################################
import boto3
from pprint import pprint
from botocore.exceptions import ClientError

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year':year, 'title':title})

    except ClientError as e:
        print(e.response['Error']['Message'])

    else:
        return response['Item']

if __name__ == "__main__":
    movie = get_movie('The Boondock Saints', 1999)
    if movie:
        pprint(movie)


### ./4.+UpdateData.py #####################################
import boto3
from pprint import pprint
from decimal import Decimal

def update_movie(title, year, rating, plot, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year':year,
            'title':title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues = {
            ':r': Decimal(rating),
            ':p': plot,
        },

        ReturnValues='UPDATED_NEW'
    )

    return response

if __name__ == "__main__":
    update_response = update_movie(
        "The Shawshank Redemption", 1994, "5.4", "This is just for testing"
    )

    pprint(update_response)


### ./5.+DeleteMovie.py #####################################
import boto3
from pprint import pprint
from botocore.exceptions import ClientError

def delete_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    try:
        response = table.delete_item(
            Key={
                'year':year,
                'title':title
            }
        )

    except ClientError as e:
        print(e.response['Error']['Message'])

    else:
        return response

if __name__ == "__main__":
    delete_response = delete_movie("Now You See Me", 2013)

    if delete_response:
        pprint(delete_response)


### ./6.+GetWithQuery.py  #####################################
import boto3
from boto3.dynamodb.conditions import Key

def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )

    return response['Items']

if __name__ == "__main__":
    query_year=1997
    print("Movies from {} ".format(query_year))

    movies = query_movies(query_year)

    for movie in movies:
        print(movie['year'], ":", movie['title'])