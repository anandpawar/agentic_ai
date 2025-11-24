import os, openai
import asyncio

openai.api_key = os.getenv('OPENAI_API_KEY')

class SummarizeAgent:
    def __init__(self):
        pass

    async def run(self, paper):
        title = paper.get('title')
        abstract = paper.get('summary') or paper.get('abstract') or ''
        if not openai.api_key:
            paper['summary_md'] = (abstract[:800] + '...') if abstract else ''
            return paper
        prompt = f"""You are a concise paper summarizer. Produce: 1) one-sentence TL;DR, 2) three bullets of key contributions, 3) why it matters.\nTitle: {title}\nAbstract: {abstract}\nRespond in markdown."""
        loop = asyncio.get_event_loop()
        resp = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
            model=os.getenv('LLM_MODEL','gpt-4o-mini'),
            messages=[{'role':'user','content':prompt}],
            max_tokens=400,
            temperature=0.1
        ))
        paper['summary_md'] = resp['choices'][0]['message']['content']
        return paper
