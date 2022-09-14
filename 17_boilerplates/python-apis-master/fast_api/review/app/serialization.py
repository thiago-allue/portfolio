from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    username: str
    email: str
    password: str


class Response(BaseModel):
    username: str
    email: str


@app.post('/login', response_model=Response)
async def login(req: Request):
    if req.username == 'username' and req.password == 'password':
        return req
    return {'message': 'Authentication Failed'}
