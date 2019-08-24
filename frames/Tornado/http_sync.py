from tornado.httpclient import HTTPClient

def synchronous_visit():
	http_client = HTTPClient()
	response = http_client.fetch("www.baidu.com"). #阻塞，直到对www.baidu.com访问完成
	print(response.body)