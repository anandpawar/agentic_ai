from fastapi import FastAPI, Query
import requests
import xml.etree.ElementTree as ET

app = FastAPI(title='MCP - external adapters')

@app.get('/arxiv/search')
def arxiv_search(query: str = Query(...), limit: int = 10):
    base = 'http://export.arxiv.org/api/query'
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': limit,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    r = requests.get(base, params=params, timeout=10)
    items = []
    try:
        root = ET.fromstring(r.text)
        ns = {'atom':'http://www.w3.org/2005/Atom'}
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns).text
            summary = entry.find('atom:summary', ns).text
            link = entry.find('atom:id', ns).text
            updated = entry.find('atom:updated', ns).text
            authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
            items.append({'title': title, 'summary': summary, 'url': link, 'updated': updated, 'authors': authors, 'source':'arXiv'})
    except Exception:
        pass
    return items

@app.get('/semantic/search')
def semantic_search(query: str, limit: int = 10):
    url = 'https://api.semanticscholar.org/graph/v1/paper/search'
    params = {'query': query, 'limit': limit, 'fields': 'title,abstract,year,citationCount,url,authors'}
    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json().get('data', [])
        items = []
        for it in data:
            items.append({
                'title': it.get('title'),
                'abstract': it.get('abstract'),
                'year': it.get('year'),
                'citationCount': it.get('citationCount'),
                'url': it.get('url'),
                'authors': [a.get('name') for a in it.get('authors', [])],
                'source':'SemanticScholar'
            })
        return items
    except Exception:
        return []
