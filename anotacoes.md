## Passo a passo:

- O projeto será em python
- No codespace o python ja vem instalado de forma padrão - Terminal -> `python3 --version`

- PASSO 1: criar .python-version
  - Terminal -> touch .python-version
  - No arquivo criado passar a versão `3.12.1`
- PASSO 2:Criação do arquivo `pyproject.toml`

  - Craiação arquivo `pyproject.toml`

- PASSO 3:
  - Criação ambiente virtual - Terminal -> python3 -m venv .venv
  - Ativar ambiente virtual - Terminal -> source .venv/bin/activate
  - Instalar pendencias inicias
    - Terminal -> pip install requests python-dotenv pydantic
    - Vamos instalar Black (formatador) e pytest (testes) dentro do .venv
      - Terminal -> pip install black pytest
    - Criação do arquivo requirements - Terminal-> pip freeze > requirements.txt
