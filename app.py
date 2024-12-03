from flask import Flask, render_template, jsonify
from elasticsearch import Elasticsearch

# Flask app initialization
app = Flask(__name__)

# Elasticsearch connection settings
CLOUD_URL = "https://newproj-fd77ee.es.us-east-1.aws.elastic.cloud:443"  # Replace with your Elasticsearch Cloud URL
API_KEY = "aDZQcmlaTUJBNzlXR3dkMWwyNTg6aDJiaTh6c1VTMFNQOFIyUV8xZUFLUQ=="  # Replace with your actual API Key
INDEX_NAME = "workplace_index"  # Replace with your index name

# Initialize Elasticsearch client
es = Elasticsearch(
    CLOUD_URL,
    api_key=API_KEY,
    verify_certs=True
)

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/data')
def get_data():
    """Fetch data from Elasticsearch and return it as JSON."""
    try:
        # Fetch all documents from the specified index
        response = es.search(index=INDEX_NAME, body={"query": {"match_all": {}}}, size=1000)
        data = [doc['_source'] for doc in response['hits']['hits']]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/search', methods=['GET'])
@app.route('/search', methods=['GET'])
def search_data():
    """Search Elasticsearch index with flexible queries."""
    from flask import request
    query = request.args.get('query', '').strip()

    if not query:
        return jsonify({"error": "Query parameter is missing"}), 400

    try:
        # Use `multi_match` to search across all fields
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["*"],  # Search across all fields
                    "fuzziness": "AUTO"  # Allow fuzzy matching for typos
                }
            }
        }

        response = es.search(index=INDEX_NAME, body=body, size=100)
        data = [doc['_source'] for doc in response['hits']['hits']]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
