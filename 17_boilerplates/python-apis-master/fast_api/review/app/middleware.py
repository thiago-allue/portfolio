import time

from fastapi import FastAPI, Request


app = FastAPI()


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f'request processed in {process_time} s')
    return response
