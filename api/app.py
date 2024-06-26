from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .schemas import Message, UserPublic, UserSchema, userDB

app = FastAPI()

# mock database
databases: list = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = userDB(id=len(databases) + 1, **user.model_dump())
    databases.append(user_with_id)
    return user_with_id


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
