import os, asyncio, requests
from typing import List, Dict, Any

MCP_URL = os.getenv('MCP_URL', 'http://localhost:9000')

class SearchAgent:
    def __init__(self):
        pass

    async def run(self, topic: str, per_source: int = 20) -> List[Dict[str, Any]]:
        loop = asyncio.get_event_loop()
        arxiv_fut = loop.run_in_executor(None, requests.get, f"{MCP_URL}/arxiv/search?query={topic}&limit={per_source}")
        ss_fut = loop.run_in_executor(None, requests.get, f"{MCP_URL}/semantic/search?query={topic}&limit={per_source}")
        resp_a, resp_s = await asyncio.gather(arxiv_fut, ss_fut)
        results = []
        try:
            results.extend(resp_a.json())
        except Exception:
            pass
        try:
            results.extend(resp_s.json())
        except Exception:
            pass
        return results
