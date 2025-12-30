from fastapi import FastAPI 
from app.schemas.jogador import Jogador, JogadorCreate
from app.db.session import engine
from app.db.base import Base
from app.models import jogador

app = FastAPI(title="API Tênis Brasileiro")
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/jogadores", response_model = list[Jogador])
def listar_jogadores():
    return [
        {"id": 1, "nome": "Thiago Monteiro", "sexo": "M"}
    ]

@app.post("/jogadores", response_model = Jogador)
def cria_jogador(jogador: JogadorCreate):
    jogador_com_id ={
        "id":3,
        "nome":jogador.nome,
        "sexo":jogador.sexo,
        "ranking":jogador.ranking
    }
    return jogador_com_id