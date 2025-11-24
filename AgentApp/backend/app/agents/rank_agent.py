from typing import List, Dict, Any
from app.tools.embeddings import embed_texts
import numpy as np

class RankAgent:
    def __init__(self):
        pass

    async def run(self, papers: List[Dict[str,Any]], query: str, top_k: int = 5) -> List[Dict[str,Any]]:
        if not papers:
            return []
        texts = [p.get('title','') + ' . ' + (p.get('summary') or p.get('abstract') or '') for p in papers]
        emb = embed_texts(texts)
        q_emb = embed_texts([query])[0]
        def cos_sim(a,b):
            return float(np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10))
        scores = []
        for i,p in enumerate(papers):
            s = cos_sim(emb[i], q_emb)
            scores.append((s,i))
        scores.sort(reverse=True)
        ranked = [papers[i] for (_,i) in scores[:top_k]]
        return ranked
