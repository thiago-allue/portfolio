import time
import multiprocessing
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index page'


def server():
    app.run(host='0.0.0.0', port=8080)


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
