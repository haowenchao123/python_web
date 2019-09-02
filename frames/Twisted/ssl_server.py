from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

class EchoServer(Protocol):
	def dataReceived(self, data):
		self.transport.write(data)

if __name__ == '__main__':
	factory = Factory()
	factory.protocol = EchoServer
	reactor.listenSSL(8007, factory, ssl.DefaultOpenSSLContextFactory('../ssl/server/key', '../ssl/server.crt'))
	reactor.run()
		