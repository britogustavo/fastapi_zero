# from http import HTTPStatus
from fastapi import FastAPI

# from fastapi_zero.schemas import Message
from fastapi.responses import HTMLResponse

app = FastAPI(title='Minha Primeira API!')


@app.get('/exercicio-html', response_class=HTMLResponse)
def exercicio_aula_02():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
        <strong><p>Testandodfjdjfdsfgfhb</p></strong>
      </body>
    </html>"""
