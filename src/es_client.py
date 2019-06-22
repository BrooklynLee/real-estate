# encoding: utf8

import pandas as pd
from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch_dsl import Q

from util import load_data

class ESClient():
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        self.es.indices.refresh(index="real-estate")
        self.s = Search(using=self.es)

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

    def _search_by_date(self, index, date):
        q = Q('bool', must=[Q('match', date=date)])
        s = self.s.query(q)
        resp = s.execute()
        return self.result2df(resp)

    def _search_by_aptname(self, index, aptname):
        q = Q('bool', must=[Q('match', 아파트=aptname)])
        s = self.s.query(q)
        resp = s.execute()
        return self.result2df(resp)

    def _search_by_rcode(self, index, rcode):
        q = Q('bool', must=[Q('match', 지역코드=rcode)])
        s = self.s.query(q)
        # resp = s.execute()
        resp = s.scan()
        return self.result2df(resp)

    # https://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html#pagination
    def _search_by_query(self, index, q):
        s = self.s.query(q)
        resp = s.scan() # to access all documents
        # resp = s.execute()
        return self.result2df(resp)

    def result2df(self, resp):
        data = []
        for h in resp:
            data.append(h.to_dict())
        df = pd.DataFrame(data)
        return  df

# bulk write
"""
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
"""
