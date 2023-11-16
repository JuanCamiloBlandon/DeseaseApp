from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import MainBot
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MensajeBot(BaseModel):
    mensaje: str

@app.get('/')
def hello_world():
    return 'Hello worlds!'


@app.post('/')
def respuesta_bot(mensaje: MensajeBot):
    return MainBot.mainBot(mensaje.mensaje)