from elasticsearch import Elasticsearch

hosts = []
es = Elasticsearch(hosts=hosts, sniff_on_start=True, sniff_on_connection_fail=True, sniffer_timeout=60, sniff_timeout=10, retry_on_timeout=True)