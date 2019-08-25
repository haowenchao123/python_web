from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient

def synchronous_visit():
	http_client = HTTPClient()
	response = http_client.fetch("www.baidu.com"). #阻塞，直到对www.baidu.com访问完成
	print(response.body)


def handle_response(response):
	print(response.body)

def asynchronous_visit():
	http_client = AsyncHTTPClient()
	http_client.fetch("www.baidu.com", callback = handle_response)