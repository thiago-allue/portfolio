import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'index': 'Index Page'}


@app.get('/{value}')
def counter_endpoint(value: int):
    return {'value': value, 'message': 'message'}


if __name__ == '__main__':
    uvicorn.run('app:app', port=8080, debug=True)
