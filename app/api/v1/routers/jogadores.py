from fastapi import Depends, APIRouter
from app.schemas.jogador import Jogador, JogadorCreate
from app.db.deps import get_db
from sqlalchemy.orm import Session
from app.services.jogador_service import listar_jogadores as listar_jogadores_service,  cria_jogador as cria_jogador_service

router = APIRouter(
    prefix="/jogadores",
    tags=["Jogadores"]
)

@router.get("/", response_model = list[Jogador])
def listar_jogadores(db: Session=Depends(get_db)):
    return listar_jogadores_service(db)

@router.post("/", response_model = Jogador)
def cria_jogador(jogador: JogadorCreate, db: Session=Depends(get_db)):
    return cria_jogador_service(db, jogador)