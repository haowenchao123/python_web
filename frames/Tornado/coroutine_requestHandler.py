import tornado.web
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
	@tornado.web.coroutine
	def get(self):
		http = tornado.httpclient.AsyncHTTPClient()
		response = yield http.fetch("http://www.baidu.com")
		self.write(response.body)