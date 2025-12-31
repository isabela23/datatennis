from fastapi import FastAPI 
from app.db.session import engine
from app.db.base import Base
from app.api.v1.routers.jogadores import router as jogadores_router

app = FastAPI(title="API Tênis Brasileiro")
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "OK"}

app.include_router(jogadores_router, prefix="/api/v1")