import time
import multiprocessing
import bottle

app = bottle.Bottle()


@app.route('/static/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='/path/to/your/static/files')


@app.route('/')
def index():
    return 'Index page'


@app.get('/login')  # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


def check_login(user, passwd):
    if user == 'user' and passwd == 'passwd':
        return True


@app.post('/login')  # or @route('/login', method='POST')
def do_login():
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def server():
    bottle.run(app=app, host='0.0.0.0', port=8080)


def processing_loop():
    t = 0
    while 1:
        time.sleep(1)
        if t == 10:
            print('Alive')
            t = 0
        t += 1


if __name__ == '__main__':
    server_process = multiprocessing.Process(target=server)
    server_process.daemon = True
    server_process.start()
    processing_loop()
