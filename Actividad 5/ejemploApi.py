from fastapi import FastAPI

# Crear una instancia de FastAPI
app = FastAPI()

# Definir una ruta raíz ("/") con el decorador @app
@app.get("/")
def read_root():
    # Devolver un diccionario con un saludo
    return {"Hello": "World"}
