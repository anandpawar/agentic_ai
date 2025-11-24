import os
from sentence_transformers import SentenceTransformer
MODEL = os.getenv('EMB_MODEL', 'all-MiniLM-L6-v2')
_model = None

def init_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL)
    return _model

def embed_texts(texts):
    m = init_model()
    arr = m.encode(texts, show_progress_bar=False, convert_to_numpy=True)
    return arr
