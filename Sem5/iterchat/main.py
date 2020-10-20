import tornado.ioloop
import tornado.web as web
import tornado.websocket
import asyncio
import json
from time import sleep
from random import choice

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

answers = ['Hi', 'how RU', 'miss you', "i'm bored", 'you', 'love', 'I', 'I <3 U', 'RU joking me?', 'sh*t', 'F...!']
seq_names = []
seq_messages = []

def render_list():
    seq_render = []
    if seq_names:
        for i in range(len(seq_names)):
            seq_render.append(f'<li><span class="name">{seq_names[i]}</span><span class="message">{seq_messages[i]}</span></li>')
    return ''.join(seq_render)

class MainHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

# class MessageBuffer():
#     def __init__(self):
#         pass

class EchoWebSocketHandler(tornado.websocket.WebSocketHandler):
    def user_message(self, message):
        data = json.loads(message)
        seq_names.append(data['name'])
        seq_messages.append(data['message'])
        lst = render_list()
        self.write_message(lst)

    def bots_answer(self):
        answer = choice(answers)
        seq_names.append('Chat Bot')
        seq_messages.append(answer)
        lst = render_list()
        self.write_message(lst)

    def chating(self, message):
        self.user_message(message)
        sleep(1)
        self.bots_answer()

    def open(self):
        print('websocket is opened')

    def on_message(self, message):
        self.chating(message)

    def on_close(self):
        print('websocket is closed')

def make_app():
    return web.Application([
        (r"/", MainHandler),
        (r"/websocket", EchoWebSocketHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, 'localhost')
    tornado.ioloop.IOLoop.current().start()