# import json
import random
import asyncio

from fastapi import FastAPI
from fastapi import Request
from fastapi import WebSocket
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


def gen():
    while 1:
        base = random.randint(10, 100)
        print(base)
        yield dict(value=base)

# with open('measurements.json', 'r') as file:
    # measurements = iter(json.loads(file.read()))
# d = list(np.random.randn(100))
measurements = (i for i in gen())

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(0.1)
        payload = next(measurements)
        await websocket.send_json(payload)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
