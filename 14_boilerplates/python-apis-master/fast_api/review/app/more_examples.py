from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


def process_file(filename: str):
    import time
    time.sleep(3)


@app.post('/upload/{filename}')
async def upload_and_process(filename: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_file, filename)
    return {'message': 'processing file'}
