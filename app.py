from fastapi import FastAPI
from models.schemas import Message
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", status_code=200, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.get("/html", status_code=200, response_class=HTMLResponse)
def read_root_html():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
