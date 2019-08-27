from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

@gen.coroutine
def coroutine_visit():
	http_client = AsyncHTTPClient()
	response = yield http_client.fetch("www.baidu.com")
	print(response.body)

@gen.coroutine
def outer_coroutine():
	print("start call another coroutine")
	yield coroutine_visit()
	print("end of outer_coroutine")

def func_normal():
	print("start to call a coroutine")
	IOLoop.current().run_sync(lambda: coroutine_visit())
	print("end of calling a coroutine")

#当Tornando程序已经处于running状态时的协程函数的调用示例如下：
def func_normal():
	print("start to call a coroutine")
	IOLoop.current().spawn_callback(coroutine_visit)
	print("end of call a coroutine")