from sqlalchemy.orm import Session
from app.models.jogador import Jogador as JogadorModel
from app.schemas.jogador import JogadorCreate


def listar_jogadores(db: Session):
    return db.query(JogadorModel).all()

def cria_jogador(db: Session, jogador: JogadorCreate):
    db_jogador = JogadorModel(
        nome = jogador.nome,
        sexo = jogador.sexo,
        ranking = jogador.ranking
    )

    db.add(db_jogador)
    db.commit()
    db.refresh(db_jogador)
    return db_jogador