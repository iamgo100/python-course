import buffer
import helpfunc as hf
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

class Buffer():
    def __init__(self):
        buffer.create_tables()

class StartHandler(web.RequestHandler):
    def get(self):
        self.render('autorization.html')

class AutorizationHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('autorization is opened')  

    def on_message(self, message):
        data = json.loads(message)
        name = data["name"]
        WebSocketHandler.name = name

    def on_close(self):
        print('autorization is closed')

# class ChatListHandler(web.RequestHandler):
#     def get(self):
#         self.render('chats.html')

class MainHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    name = ''

    def user_message(self, message):
        data = json.loads(message)
        seq_names.append(data['name'])
        seq_messages.append(data['message'])
        lst = hf.render_list(seq_names, seq_messages)
        self.write_message(lst)

    def bots_answer(self):
        answer = choice(answers)
        seq_names.append('Chat Bot')
        seq_messages.append(answer)
        lst = hf.render_list(seq_names, seq_messages)
        self.write_message(lst)

    def chating(self, message):
        self.user_message(message)
        sleep(1)
        self.bots_answer()

    def open(self):
        print('start chating')
        lst = hf.render_list(seq_names, seq_messages)
        self.write_message(lst)

    def on_message(self, message):
        self.chating(message)

    def on_close(self):
        print('end chating')

def make_app():
    return web.Application([
        (r"/", StartHandler),
        # (r"/chats", ChatListHandler),
        (r"/index", MainHandler),
        (r"/websocket", WebSocketHandler),
        (r"/autorization", AutorizationHandler)
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, 'localhost')
    tornado.ioloop.IOLoop.current().start()