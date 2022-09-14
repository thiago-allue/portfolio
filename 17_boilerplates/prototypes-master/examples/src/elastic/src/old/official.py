from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')

doc = {
    'author': 'author_name',
    'text': 'Interesting content...',
    'timestamp': datetime.now(),
}
resp = es.index(index="test-index", id=1, body=doc)
print(resp['result'])

resp = es.get(index="test-index", id=1)
print(resp['_source'])

es.indices.refresh(index="test-index")

# res = es.search(index="test-index", query={"match_all": {}})
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

doc = {
    'author': 'author_name',
    'text': 'Interesting modified content...',
    'timestamp': datetime.now(),
}
resp = es.update(index="test-index", id=1, body=doc)
print(resp['result'])

es.delete(index="test-index", id=1)