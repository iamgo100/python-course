import helpfunc as hf
import tornado.ioloop
import tornado.web as web
import tornado.websocket
import asyncio
import json
from tornado.locks import Condition
from time import sleep
from random import choice

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
          instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Buffer:
    def __init__(self):
        self.__name = ''
        self.__messages = []
        self.__answers = ['Hi', 'how RU', 'miss you', "i'm bored", 'you', 'love', 'I', 'I <3 U', 'RU joking me?', 'sh*t', 'F...!']

        self.condition = Condition()

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    def add_message(self, name, message):
        self.__messages.append({"name": name, "message": message})
        self.condition.notify_all()
    
    def get_answer(self):
        return choice(self.__answers)

    def render(self):
        return hf.render_list(self.__messages)
    
    def get_users_messages(self, cursor):

        return hf.render_list("sth")

class StartHandler(web.RequestHandler):
    def get(self):
        self.render('autorization.html')

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

buffer = Buffer()

class MainHandler(tornado.websocket.WebSocketHandler):
    def user_message(self, data):
        buffer.add_message(buffer.get_name(), data['message'])
        self.write_message(buffer.render())

    def bots_answer(self):
        buffer.add_message('Chat Bot', buffer.get_answer())
        self.write_message(buffer.render())

    def chating(self, message):
        self.user_message(message)
        sleep(1)
        self.bots_answer()

    def open(self):
        print('websocket is open')
        self.write_message(buffer.render())

    def on_message(self, message):
        data = json.loads(message)
        if data.get("message"):
            self.chating(data)
        else:
            buffer.set_name(data["name"])

    def on_close(self):
        print('websocket is close')

def make_app():
    return web.Application([
        (r"/", StartHandler),
        (r"/index", IndexHandler),
        (r"/websocket", MainHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, 'localhost')
    tornado.ioloop.IOLoop.current().start()