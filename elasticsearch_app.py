from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Create an index called "my_index"
es.indices.create(index='my_index')

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