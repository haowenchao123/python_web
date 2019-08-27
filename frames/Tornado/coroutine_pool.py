from concurrent.futures import ThreadPoolExecutor
from tornado import gen

thread_pool = ThreadPoolExecutor(2)

def mySleep(count):
	import time
	for I in range(count):
		time.sleep(1)

@gen.coroutine
def call_blocking():
	print("start of call_blocking")
	yield thread_pool.submit(mySleep, 10)
	print("end of call_blocking")

if __name__ == '__main__':
	call_blocking()