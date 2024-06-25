from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .schemas import Message, UserPublic, UserSchema

app = FastAPI()


@app.get("/", status_code=200, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post("/users/", response_model=UserPublic)
def create_user(user: UserSchema):
    return user


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
