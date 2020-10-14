import tornado.ioloop
import tornado.web as web
import tornado.websocket
import asyncio
import json
from random import randint, choice

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

answers = ['Hi', 'how RU', 'miss you', "i'm bored", 'you', 'love', 'I', 'I <3 U', 'RU joking me?', 'sh*t', 'F...!']
seq_names = []
seq_messages = []

def render_list(message):
    data = json.loads(message)
    seq_names.append(data['name'])
    seq_messages.append(data['message'])
    seq_render = []
    if seq_names:
        for i in range(len(seq_names)):
            seq_render.append(f'<li><span class="name">{seq_names[i]}</span><span class="message">{seq_messages[i]}</span></li>')
    return ''.join(seq_render)

class MainHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

class EchoWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('websocket is opened')

    def on_message(self, message):
        lst = render_list(message)
        self.write_message(lst)

    def on_close(self):
        print('websocket is closed')
        tornado.ioloop.IOLoop.current().stop()

def make_app():
    return web.Application([
        (r"/", MainHandler),
        (r"/websocket", EchoWebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, 'localhost')
    tornado.ioloop.IOLoop.current().start()