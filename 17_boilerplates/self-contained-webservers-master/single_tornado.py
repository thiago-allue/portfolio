import time
import multiprocessing
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('MainHandler')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])


def server():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


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
