import tornado.ioloop
import tornado.web

class MainHandle(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello World")

def make_app():
		return tornado.web.Application([
			(r"/", MainHandle)
			])

def main():
		app = make_app()
		app.listen(8888)
		tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
	main()


		