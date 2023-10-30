
#Install elastic search in WSL Debian with docker.
# Reference:
# https://www.elastic.co/guide/en/elasticsearch/reference/7.17/docker.html
# Optional references:
#  - https://askubuntu.com/questions/1427872/running-elasticsearch-on-ubuntu-on-wsl-system-has-not-been-booted-with-systemd


# Run docker and elasticsearch should automatically started in WSL Linux
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
    print(f"Creating index 'my_index' ...")
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
print('Preparing a list of index operations for bulk indexing')
actions = [
    {
        '_op_type': 'index',  # Operation type for indexing
        '_index': 'my_index',  # Target index
        '_id': doc_id,  # Document ID
        '_source': document  # Document data
    }
    for doc_id, document in enumerate(documents, start=1)
]

# Measure the time taken to perform the bulk indexing
start_time = time.time()
# Use the bulk helper to perform the bulk indexing
success, failed = bulk(es, actions)
print("Waiting...success %s, failed %s" %(success, failed))
end_time = time.time()
indexing_time = end_time - start_time

# Check the results
if failed:
    print(f"Failed operations:")
    for item in failed:
        print(f"Operation failed: {item}")
else:
    print(f"All {success} operations were successful.")

# Measure the time taken to perform the index refresh
start_time = time.time()
# Refresh the index to make the data immediately available for search
print("Refreshing the index...")
es.indices.refresh(index='my_index')
end_time = time.time()
refresh_time = end_time - start_time

print(f"Bulk indexing time: {indexing_time} seconds")
print(f"Index refresh time: {refresh_time} seconds")

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
    print('Found! ', hit['_source'])

# Delete the index
es.indices.delete(index='my_index')