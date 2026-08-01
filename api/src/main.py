import os
from fastapi import FastAPI
from dotenv import load_dotenv
import src.database as db

load_dotenv() # Carrega o .env

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API está rodando!", "user": os.getenv("DB_USER")}

@app.get("/status-db")
def check_db():
    if db.test_connection():
        return {"status": "success", "message": "Conectado ao Postgres com sucesso!"}
    else:
        return {"status": "error", "message": "Falha na conexão com o banco."}
