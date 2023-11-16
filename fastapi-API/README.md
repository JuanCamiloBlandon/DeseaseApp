# Creación de entorno VirtualPython

```sh
# Para el entorno virtual es necesario usar una terminal
# (Puede ser la de preferencia o Gitbash)

python -m venv venv

# Para activar el entorno utilizamos el siguiente comando:
# Windows
source venv/Scripts/activate
# Linux
source venv/bin/activate

# Luego instalamos los requerimentos con el siguiente comando:
pip install -r requirements.txt

# Ya con esto podemos correr nuestro servidor de FastAPI
uvicorn main:app --reload
```
