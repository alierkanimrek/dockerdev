import tornado.ioloop
import tornado.web
from tornado import gen
import motor




class MainHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        client = motor.MotorClient(host='172.18.0.3', port=27017)
        info = yield client.server_info()
        self.write("<h2>Hello world</h2>")
        self.write("<h3>MongoDB</h3>")
        for item in info.items():
            self.write(str(item[0])+" : "+str(item[1])+"</br>")




def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])



if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()