import time

import uvicorn

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.background import BackgroundTasks

app = Starlette()

@app.route('/user/signup', methods=['POST', 'GET'])
async def signup(request):
    print(request.method)
    if request.method == 'POST':
        data = await request.json()
        if data:
            username = data['username']
            email = data['email']
    else:
        username = 'user'
        email = 'email'
    tasks = BackgroundTasks()
    tasks.add_task(send_welcome_email, to_address=email)
    tasks.add_task(send_admin_notification, username=username)
    message = {'status': 'Signup successful'}
    return JSONResponse(message, background=tasks)

async def send_welcome_email(to_address):
    print('start send welcome email')
    time.sleep(3)
    print('end send welcome email')

async def send_admin_notification(username):
    print('start send admin notification')
    time.sleep(3)
    print('end send admin notification')


def main():
    uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
