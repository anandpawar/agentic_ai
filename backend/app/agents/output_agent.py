import os, json, datetime

class OutputAgent:
    def __init__(self, store_path: str = './outputs'):
        self.store_path = store_path
        os.makedirs(self.store_path, exist_ok=True)

    async def run(self, papers, topic):
        fname = f"top5_{topic.replace(' ','_')}_{datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
        path = os.path.join(self.store_path, fname)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(papers, f, indent=2)
        return path
