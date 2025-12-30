from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Jogador(Base):
    __tablename__ = "jogadores"

    id: Mapped[int] = mapped_column(Integer, primary_key =True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    sexo: Mapped[str]=mapped_column(String, nullable=False)
    ranking: Mapped[int | None] = mapped_column(Integer)

    