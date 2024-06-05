from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World!"}                                     #TIPOS DE PARAMETROS DE UNA RUTA: A)RUTA / B)CONSULTA ?,&

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}                     #http://localhost:8000/items/1000?q=mouse  ejemplo de uso

@app.get('/calculadora')
def calcular (operando_1: float, operando_2: float):
      return {'suma': operando_1 + operando_2}                   #http://localhost:8000/calculadora?operando_1=10&operando_2=25 



