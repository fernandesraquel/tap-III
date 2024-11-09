import Pyro5.api

@Pyro5.api.expose
class Calculadora:
  def soma(self, x, y): return x + y
  def subtracao(self, x, y): return x - y
  def multiplicacao(self, x, y): return x * y
  def divisao(self, x, y): return x / y if y != 0 else -1

daemon = Pyro5.api.Daemon()  # Inicializa o daemon Pyro
ns = Pyro5.api.locate_ns(host="localhost", port=9090)   # Conecta ao nameserver
uri = daemon.register(Calculadora)
ns.register("calculadora.remota", uri)

print("Servidor RMI aguardando requisições...")
daemon.requestLoop()

