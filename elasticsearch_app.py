from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}], timeout=3)
try:
    if es.ping():
        print("Successfully connected to Elasticsearch")
    else:
        raise ConnectionError("Failed to connect to Elasticsearch")
except ConnectionError as e:
    print(f"Connection error: {str(e)}")


index_name = 'my_index'
# Create the index with a custom timeout
try:
    es.indices.create(index=index_name, timeout='10s')
    print(f"The index '{index_name}' was created successfully.")
except Exception as e:
    print(f"Failed to create the index '{index_name}': {str(e)}")

# Index a document in "my_index"
document = {
    'title': 'Sample Document',
    'content': 'This is a sample document for Elasticsearch in Python.'
}


es.index(index='my_index', doc_type='_doc', id=1, body=document)

# Search for documents containing the term "content"
search_query = {
    'query': {
        'match': {
            'content': 'Elasticsearch Python'
        }
    }
}

response = es.search(index='my_index', body=search_query)

# Print the search results
for hit in response['hits']['hits']:
    print(hit['_source'])

# Delete the index
es.indices.delete(index='my_index')