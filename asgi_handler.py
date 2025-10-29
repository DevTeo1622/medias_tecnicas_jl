from fastapi import FastAPI
from main import app  # importa tu app FastAPI

# Vercel necesita que el archivo exponga una variable llamada `handler`
# que sea una función ASGI compatible
handler = app
