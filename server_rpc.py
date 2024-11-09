# Importa a classe para criar o servidor XML-RPC
from xmlrpc.server import SimpleXMLRPCServer  

def soma(x, y): return x + y
def subtracao(x, y): return x - y
def multiplicacao(x, y): return x * y
def divisao(x, y): return x / y if y != 0 else -1

# Cria o servidor XML-RPC que escutará no endereço localhost e na porta 8000
server = SimpleXMLRPCServer(("localhost", 8000))

# Registra as funções no servidor, associando cada função a um nome de chamada remota
server.register_function(soma, "soma")                     
server.register_function(subtracao, "subtracao")          
server.register_function(multiplicacao, "multiplicacao")   
server.register_function(divisao, "divisao")               

# Exibe mensagem informando que o servidor está aguardando requisições
print("Servidor RPC aguardando requisições...")

# Mantém o servidor em execução contínua, aguardando chamadas de clientes
server.serve_forever()

