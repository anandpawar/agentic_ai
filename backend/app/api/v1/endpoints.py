from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.search_agent import SearchAgent
from app.agents.rank_agent import RankAgent
from app.agents.summarize_agent import SummarizeAgent
from app.agents.output_agent import OutputAgent

router = APIRouter()

class Query(BaseModel):
    topic: str
    count: int = 5

@router.post('/search')
async def search(q: Query):
    searcher = SearchAgent()
    ranker = RankAgent()
    summarizer = SummarizeAgent()
    output = OutputAgent()
    found = await searcher.run(q.topic, per_source=20)
    ranked = await ranker.run(found, q.topic, top_k=q.count)
    import asyncio
    tasks = [summarizer.run(p) for p in ranked]
    summarized = await asyncio.gather(*tasks)
    outpath = await output.run(summarized, q.topic)
    return {'path': outpath, 'results': summarized}
