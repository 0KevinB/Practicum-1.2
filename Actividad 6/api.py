from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from aplicacion import process_text

# Crear una instancia de FastAPI
app = FastAPI()

# Agregar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todas las cabeceras
)

# Definir la ruta "/analyze/" con el método POST
@app.post("/analyze/")
async def process_text_endpoint(textos: List[str]):
    # Llamar a la función process_text para procesar los textos
    return process_text(textos)
