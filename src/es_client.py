from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

from util import read_csv
from util import load_data

class ESClient():
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def _bulk(self, docs):
        res = helpers.bulk(self.es, docs)
        print (res)

    def _put(self, index, dtype, id, doc):
        res = self.es.index(index=index, doc_type=dtype, id=id, body=doc)
        print (res)
    
    def _get(self, index, dtype, id):
        res = es.get(index=index, doc_type=dtype, id=id)
        print(res)
    
    def _query(self, index, query):
        # es.indices.refresh(index=index)
        res = self.es.search(index=index, body=query)
        return res

# bulk write

df =  load_data('41131', 'trade')
# convert pandas dataframe to list of dict
items = df.to_dict('records')
print ('# of items : %s' % (len(items)))
# data = [item.update({'timestamp': datetime.now()}) for item in items]
docs = []
for item in items:
    docs.append({
        '_index': 'real-estate',
        '_type': 'trade',
        '_id': datetime.now(),
        '_source': item
    })
es = ESClient()
es._bulk(docs)

# query results

import pandas as pd
es = ESClient()
results = es._query('real-estate', {"query": {"match": { "아파트": "삼정그린뷰"}}})
items = results['hits']['hits']
df = pd.DataFrame([x['_source'] for x in items])
print (df)
# es._query('real-estate', {"query": {"match_all": {}}})
