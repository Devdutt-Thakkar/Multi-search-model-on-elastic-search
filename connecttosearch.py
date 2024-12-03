from elasticsearch import Elasticsearch

# Replace with your Elasticsearch Cloud credentials
CLOUD_URL = "https://newproj-fd77ee.es.us-east-1.aws.elastic.cloud:443"
API_KEY = "Z2FQTGlKTUJBNzlXR3dkMVltN206VXNwcFFxbDFScDJDd2tYcnhuekZzdw=="  # Replace with your actual API Key
INDEX_NAME = "workplace_index"  # Replace with your index name

# Initialize Elasticsearch client
es = Elasticsearch(
    CLOUD_URL,
    api_key=API_KEY,
    verify_certs=True
)

try:
    # Test the connection
    if es.ping():
        print("Successfully connected to Elasticsearch Cloud!")
    else:
        print("Connection to Elasticsearch failed.")

    # Fetch all documents from the specified index
    response = es.search(index=INDEX_NAME, body={"query": {"match_all": {}}}, size=1000)

    # Display the documents
    print(f"Total documents found: {response['hits']['total']['value']}")
    for doc in response['hits']['hits']:
        print(doc['_source'])

except Exception as e:
    print(f"An error occurred: {e}")
