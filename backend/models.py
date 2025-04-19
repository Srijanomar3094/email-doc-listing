from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class Email(BaseModel):
    sender: str
    subject: str
    timestamp: str
    attachments: list[str]
