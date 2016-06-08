from elasticsearch import Elasticsearch

es = Elasticsearch()
res = es.search(index="app", body={"fields":["title"],"size":1,"query": {"query_string": {"query":"fdsfsd"}}})
print res['hits']['total']
