# Deployment

Use Gunicorn and uvicorn, to have multiple async processing serving and dispatching requests.

`gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app`
