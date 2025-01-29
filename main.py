from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hola_mundo():
    return{"hola : mundo"}

@app.get('/primerget/{id_usuario}')
def primer_get(id: int, valor: Union[str,None]= None):
    return{"id":id, "valor": valor}
