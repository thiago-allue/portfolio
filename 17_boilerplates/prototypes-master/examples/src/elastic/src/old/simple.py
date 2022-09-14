from elasticsearch import Elasticsearch

elastic_client = Elasticsearch(hosts=["localhost"])

query_body = {"query": {"match": {"some_field": "search_for_this"}}}

# elastic_client.search(index="some_index", body=some_query)

result = elastic_client.search(index="some_index", body={"query": {"match_all": {}}})

user_request = "some_param"

# Take the user's parameters and put them into a
# Python dictionary structured as an Elasticsearch query:
query_body = {"query": {"bool": {"must": {"match": {"some_field": user_request}}}}}

# Pass the query dictionary to the 'body' parameter of the
# client's Search() method, and have it return results:
result = elastic_client.search(index="some_index", body=query_body)



result = elastic_client.search(index="some_index", body=query_body)
print ("query hits:", result["hits"]["hits"])

result = elastic_client.search(index="some_index", body=query_body, size=999)
print ("total hits:", len(result["hits"]["hits"]))