from xmlrpc.server import SimpleXMLRPCServer

def soma(x, y): return x + y
def subtracao(x, y): return x - y
def multiplicacao(x, y): return x * y
def divisao(x, y): return x / y if y != 0 else -1

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(soma, "soma")
server.register_function(subtracao, "subtracao")
server.register_function(multiplicacao, "multiplicacao")
server.register_function(divisao, "divisao")

print("Servidor RPC aguardando requisições...")
server.serve_forever()
