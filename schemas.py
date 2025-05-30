from pydantic import BaseModel, EmailStr

class UserClient(BaseModel):
    username: str
    email: EmailStr

