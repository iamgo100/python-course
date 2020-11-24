import tornado.ioloop
import tornado.web as web
import tornado.websocket
import asyncio
import json
from tornado.locks import Condition

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
        self.__messages = []
        self.__name = ''

        self.condition = Condition()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def add_message(self, name, message):
        import uuid
        id = uuid.uuid4()
        self.__messages.append({'id': str(id), "name": name, "message": message})
        self.condition.notify_all()
    
    def get_messages_since(self, cursor):
        results = []

        for msg in reversed(self.__messages):
            if msg['id'] == cursor:
                break
            results.append(msg)
        results.reverse()
        return results

    def render(self):
        seq_render = []
        seq = self.__messages
        if seq:
            for i in range(len(seq)):
                seq_render.append(f'<li><span class="name">{seq[i]["name"]}</span><span class="message">{seq[i]["message"]}</span></li>')
        return json.dumps({"messages": ''.join(seq_render)})

class StartHandler(web.RequestHandler):
    def get(self):
        self.render('autorization.html')

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

buffer = Buffer()

class MainHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print('new websocket is open')
        self.write_message(buffer.render())

    def on_message(self, message):
        data = json.loads(message)
        print(data)
        if data.get("message"):
            buffer.add_message(data["name"], data['message'])
            self.write_message(buffer.render())
        elif data.get("request"):
            if data["request"] == "get name":
                name = {"setName": buffer.get_name()}
                self.write_message(json.dumps(name))
            if data["request"] == "update":
                self.write_message(buffer.render())
        else:
            buffer.set_name(data["name"])

    def on_close(self):
        print('some websocket is close')

class MessageUpdateHandler(tornado.websocket.WebSocketHandler):
    pass

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