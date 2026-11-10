import asyncio
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class TermesHandler(tornado.web.RequestHandler):
    def post(self):
        checked = self.get_body_argument("accept_terms", None)
        if hecked == "yes":
            self.write("OK")
        else:
            self.write("KO")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),    # call MainHandler in /
        (r"/submit", TermesHandler),    # call TermesHandler in /submit
    ])

async def main():
    app = make_app()
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__=="__main__":
    asyncio.run(main())
