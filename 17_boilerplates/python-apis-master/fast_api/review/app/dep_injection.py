# from databases import Database
from fastapi import FastAPI, Depends
from starlette.requests import Request

# from db_helpers import get_all_data


class Database:
    pass


def get_all_data():
    pass


def get_db(request: Request):
    return request.app.state._db


app = FastAPI()


@app.get('/data')
def get_data(db: Database = Depends(get_db)):
    return get_all_data(db)
