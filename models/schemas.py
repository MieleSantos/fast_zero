from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class userSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
