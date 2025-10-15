from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

load_dotenv()
URL_DATABASE = os.getenv("URL_DATABASE")

if not URL_DATABASE:
    raise ValueError(
        "URL_DATABASE No está configurada"
    )

#postgresql://postgres.sswqxodpgdacijwseerb:v7gm8TE8RidxbCMX@aws-1-sa-east-1.pooler.supabase.com:6543/postgres

cadena_de_conexion = f"postgresql://postgres.sswqxodpgdacijwseerb:v7gm8TE8RidxbCMX@aws-1-sa-east-1.pooler.supabase.com:5432/postgres"

engine = create_engine("postgresql://postgres.sswqxodpgdacijwseerb:v7gm8TE8RidxbCMX@aws-1-sa-east-1.pooler.supabase.com:5432/postgres")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    with SessionLocal() as session:
        yield session

SessionDepends = Annotated[Session, Depends(get_db)]