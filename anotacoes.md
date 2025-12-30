## Passo a passo:

- O projeto será em python
- No codespace o python ja vem instalado de forma padrão - Terminal -> `python3 --version`

- PASSO 1: criar .python-version

  - Terminal -> touch .python-version
  - No arquivo criado passar a versão `3.12.1`

- PASSO 2:

  - Criação ambiente virtual - Terminal -> `python -m venv .venv`
  - Ativar ambiente virtual - Terminal -> `source .venv/bin/activate`

- PASSO 3: Instalação do fastAPI - > `pip install fastapi uvicorn`

- PASSO 4:

  - Criação da pasta app e do arquivo app/main.py

- PASSO 5:

  - Subir o servidor -> `uvicorn app.main:app --reload`

- PASSO 6:

  - Criação do schema (modelo de dados);
  - Criação da pasta `app/schemas` e do arquivo `app/schemas/jogador.py`

- PASSO 7:

  - Instalação das dependências do banco -> `pip install sqlalchemy psycopg[binary]`
    - sqlalchemy : ORM
    - psycopg: driver Postgres

- PASSO 8:

  - Criação da camada do banco -> Pasta - `app/db` e arquivo - `app/db/session.py`
  - Criação do arquivo `app/db/base.py`

- PASSO 9:

  - Criação do modelo do Jogador
    -> Criação da pasta - `app/models` e arquivo `app/models/jogador.py`

- PASSO 10:

  - Criação do docker do postgres
  - Criação do arquivo `docker-compose.yml`
    -> Depois pra subir -> `docker compose up -d`
    -> Pra testar se o banco esta funcionado -> `docker exec -it tenis_postgres psql -U tenis_user -d tenis`

- PASSO 11:

  - Criação arquivo `app/db/deps.py`
