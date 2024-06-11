# FastAPI

#Tutorial - Guía para el Usuario

INSTALA FastAPI:
El primer paso es instalar FastAPI.
Para el tutorial, es posible que quieras instalarlo con todas las dependencias y características opcionales:

pip install "fastapi[all]"

también incluye uvicorn que puedes usar como el servidor que ejecuta tu código.

TAMBIEN PUEDES INSTALARLO PARTE POR PARTE.
Esto es lo que probablemente harías una vez que desees implementar tu aplicación en producción: 
pip install fastapi
También debes instalar uvicorn para que funcione como tu servidor: 
pip install "uvicorn[standard]"

PRIMEROS PASOS:
Aca veremos como utilizarlo para que puedas implementar los pasos basicos que ofrece.

Un archivo muy basico de FastAPI podría verse de esta manera:

Copia el siguiente codigo en un archivo main.py.



from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def root():
    
    return {"message": "Hello World"}       



Corre el servidor en vivo:
Pega este codigo en la terminal donde tengas abierto main.py:
uvicorn main:app --reload
Si todo salio bien debebria darte el siguiente resultado en la terminal.

INFO:     Uvicorn running on http://127.0.0.1:8000

INFO:     Started reloader process [28720]

INFO:     Started server process [28722]

INFO:     Waiting for application startup.

INFO:     Application startup complete.


En caso contrario habria que solucionar el problema y ver porque estaria dando error.

#NOTA EXPLICATIVA:
El comando uvicorn main:app se refiere a:
main: el archivo main.py (el "módulo" de Python).
app: el objeto creado dentro de main.py con la línea app = FastAPI().
--reload: hace que el servidor se reinicie cada vez que cambia el código. Úsalo únicamente para desarrollo.

Seguimos con la explicación.
En el output, hay una línea que dice más o menos: 
INFO: Uvicorn running on http://127.0.0.1:8000  
#Esa línea muestra la URL dónde se está sirviendo tu app en tu maquina local.

Revísalo:
Abre tu navegador en http://127.0.0.1:8000.

Verás la respuesta en JSON: {"message": "Hello World"}





















