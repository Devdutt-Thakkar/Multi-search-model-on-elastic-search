# document_loader.py

import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def process_csv(file_path):
    # Read CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Combine all text data into a list
    content = []
    for _, row in df.iterrows():
        # Assuming the CSV has a column named 'text' containing the data
        text = ' '.join(map(str, row.values))
        content.append(text)
    
    # Split documents into passages
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=256,
    )
    docs = text_splitter.create_documents(content)
    return docs
