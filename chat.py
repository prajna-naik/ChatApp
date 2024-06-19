import tornado.ioloop  #manages non-blocking operations
import tornado.web  #tool for handling http req
import tornado.websocket        #allow real-time chat

clients = []

class ChatHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        clients.append(self)

    def on_message(self, message):
        for client in clients:
            client.write_message(message)

    def on_close(self):
        clients.remove(self)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/chat", ChatHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    print("Server is listening in port 8888")
    tornado.ioloop.IOLoop.current().start()


