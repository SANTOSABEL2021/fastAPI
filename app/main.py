import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI
from app.database import Base, engine
from routes import user

# Cria as tabelas no banco de dados.
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Adiciona as rotas de usuários.
app.include_router(user.router, prefix="/users", tags=["Users"])
