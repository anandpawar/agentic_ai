import chromadb
from chromadb.config import Settings
import os

CHROMA_DIR = os.getenv('CHROMA_DIR','./chroma_db')
client = chromadb.Client(Settings(chroma_db_impl='duckdb+parquet', persist_directory=CHROMA_DIR))

def get_collection(name='papers'):
    return client.get_or_create_collection(name)

def upsert_papers(papers):
    col = get_collection()
    ids = [p.get('id', str(i)) for i,p in enumerate(papers)]
    metadatas = [{k:v for k,v in p.items() if k not in ('summary','abstract')} for p in papers]
    embeddings = [p.get('_embedding') for p in papers]
    titles = [p.get('title','') for p in papers]
    col.add(ids=ids, metadatas=metadatas, documents=titles, embeddings=embeddings)
