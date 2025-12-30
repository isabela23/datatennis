from pydantic import BaseModel

class Jogador(BaseModel):
    id: int
    nome: str
    sexo: str
    ranking: int | None = None

class JogadorCreate(BaseModel):
    nome: str
    sexo: str
    ranking: int | None = None