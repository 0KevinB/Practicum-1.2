from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from aplicacion import process_text

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/analyze/")
async def process_text_endpoint(textos: List[str]):
    return process_text(textos)
