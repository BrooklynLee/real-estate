from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from util import read_csv

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

df = read_csv("apt-trade/41131/201201.csv")
# convert pandas dataframe to list of dict
items = df.to_dict('records')
data = [item.update({'timestamp': datetime.now()}) for item in items]

# put to es
# res = es.index(index="real-estate", doc_type='trade', id=1, body=data[0])
# print(res['result'])

# bulk to es
docs = []
for item in items:
    docs.append({
        '_index': 'real-estate',
        '_type': 'trade',
        '_id': datetime.now(),
        '_source': item
    })
helpers.bulk(es, docs)

# get from es
# res = es.get(index="real-estate", doc_type='trade', id=1)
# print(res['_source'])

# query to es
# es.indices.refresh(index="real-estate")
# res = es.search(index="real-estate", body={"query": {"match_all": {}}})

# print search result
# print (res['hits'])
