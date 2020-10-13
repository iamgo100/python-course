import tornado.ioloop
import tornado.web
import tornado.websocket
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class EchoWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('websocket is opened')
    
    def on_message(self, message):
        self.write_message(f" Message was sent: {message} ")
    
    def on_close(self):
        print('websocket is closed')
        tornado.ioloop.IOLoop.current().stop()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", EchoWebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, 'localhost')
    tornado.ioloop.IOLoop.current().start()