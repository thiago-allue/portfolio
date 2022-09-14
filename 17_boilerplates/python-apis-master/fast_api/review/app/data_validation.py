from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    username: str
    password: str


@app.post('/login')
async def login(req: Request):
    if req.username == 'username' and req.password == 'password':
        return {'message': 'success'}
    return {'message': 'Authentication Failed'}
