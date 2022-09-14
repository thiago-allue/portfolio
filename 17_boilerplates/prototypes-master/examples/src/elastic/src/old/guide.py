import requests

r = requests.get(
    "http://api.tvmaze.com/singlesearch/shows?q=big-bang-theory&embed=episodes"
)

import json

jd = json.loads(r.content)
print(jd["_embedded"]["episodes"][0])

import re

ldocs = []
for jo in jd["_embedded"]["episodes"][0:200]:
    d = {}
    d["id"] = jo["id"]
    d["season"] = jo["season"]
    d["episode"] = jo["number"]
    d["name"] = jo["name"]
    d["summary"] = re.sub("<[^<]+?>", "", jo["summary"])
    ldocs.append(d)

from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200}])


import json

# iterate through documents indexing them
for doc in ldocs:
    es.index(index="tvshows", doc_type="bigbang", id=doc["id"], body=json.dumps(doc))

es.get(index="tvshows", doc_type="bigbang", id=2915)

es.search(
    index="tvshows",
    doc_type="bigbang",
    body={"query": {"match": {"summary": "rivalry"}}},
)

es.search(
    index="tvshows", doc_type="bigbang", body={"query": {"fuzzy": {"summary": "rival"}}}
)

es.indices.delete(index="bigbang", ignore=[400, 404])
