from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
import uvicorn

app = FastAPI(title='CrewAI Top5 Papers')

app.include_router(api_router, prefix='/api/v1')

@app.get('/health')
def health():
    return {'status':'ok'}

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)
