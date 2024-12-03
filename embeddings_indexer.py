# embeddings_indexer.py

from langchain.vectorstores import ElasticVectorSearch
from elasticsearch import Elasticsearch
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_store(docs, cloud_url, api_key):
    # Use a pre-trained SentenceTransformer model
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Initialize Elasticsearch client with Cloud URL and API Key
    es = Elasticsearch(
        [cloud_url],
        api_key=api_key,
        verify_certs=True
    )
    
    # Create the vector store using from_elasticsearch_client
    vector_store = ElasticVectorSearch.from_elasticsearch_client(
        embedding=embeddings_model,
        client=es,
        index_name="uploaded-docs",
    )
    
    # Add documents to the vector store
    vector_store.add_documents(docs)
    return vector_store
