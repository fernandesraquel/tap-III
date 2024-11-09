# Importa a biblioteca Pyro5 para comunicação remota de objetos
import Pyro5.api 

# Define a classe Calculadora e expõe seus métodos para acesso remoto
@Pyro5.api.expose  # Decorador para expor a classe/métodos para chamadas remotas
class Calculadora:
  def soma(self, x, y): return x + y
  def subtracao(self, x, y): return x - y 
  def multiplicacao(self, x, y): return x * y  
  def divisao(self, x, y): return x / y if y != 0 else -1  

# Inicializa o daemon Pyro, que gerencia a comunicação de objetos remotos
daemon = Pyro5.api.Daemon()  

# Localiza o NameServer que está rodando no endereço localhost e porta 9090
ns = Pyro5.api.locate_ns(host="localhost", port=9090)  

# Registra a classe Calculadora no daemon e obtém sua URI
uri = daemon.register(Calculadora)  

# Registra o objeto remoto no NameServer com o nome "calculadora.remota"
ns.register("calculadora.remota", uri)  

# Imprime mensagem indicando que o servidor está pronto para receber requisições
print("Servidor RMI aguardando requisições...")

# Inicia o loop principal, aguardando e respondendo às requisições remotas
daemon.requestLoop()

