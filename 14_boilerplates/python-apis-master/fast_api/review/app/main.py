from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


@app.get('/')
def home():
    return {'Hello': 'GET'}


@app.post('/')
def home_post():
    return {'Hello': 'POST'}


@app.get('/employee')
def home(department: str):
    # In Flask it was request.args.get('department')
    return {'department': department}
