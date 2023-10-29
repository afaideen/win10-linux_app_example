import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Name of the index to check
index_name = 'my_index'

# Check if the index exists
if es.indices.exists(index=index_name):
    print(f"The index '{index_name}' already exists.")
else:
    print(f"The index '{index_name}' does not exist.")
    # Create an index called "my_index"
    es.indices.create(index='my_index')



# List of documents to index
documents = [
    {
        'title': 'Document 1',
        'content': 'This is the first document.'
    },
    {
        'title': 'Document 2',
        'content': 'This is the second document.'
    },
    {
        'title': 'Document 3',
        'content': 'This is the third document.'
    }
]

# Index each document in a loop
# for doc_id, document in enumerate(documents, start=1):
#     es.index(index='my_index', doc_type='_doc', id=doc_id, body=document)

# Prepare a list of index operations for bulk indexing
actions = [
    {
        '_op_type': 'index',  # Operation type for indexing
        '_index': 'my_index',  # Target index
        '_id': doc_id,  # Document ID
        '_source': document  # Document data
    }
    for doc_id, document in enumerate(documents, start=1)
]

# Use the bulk helper to perform the bulk indexing
success, failed = bulk(es, actions)
print("Waiting...")
time.sleep(2.0)
print("Start searching...)")
# Search for documents containing the term "content"
search_query = {
    'query': {
        'match': {
            'content': 'third'
        }
    }
}


response = es.search(index='my_index', body=search_query)

# Print the search results
for hit in response['hits']['hits']:
    print(hit['_source'])

# Delete the index
es.indices.delete(index='my_index')