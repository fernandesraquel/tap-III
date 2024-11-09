import paho.mqtt.client as mqtt
import json

# Funções da calculadora
def soma(x, y): return x + y
def subtracao(x, y): return x - y
def multiplicacao(x, y): return x * y
def divisao(x, y): return x / y if y != 0 else "Erro: divisão por zero"

# Callback para quando o servidor se conectar ao broker
def on_connect(client, userdata, flags, rc):
  print(f"Conectado ao broker: {rc}")
  # O servidor estará escutando o tópico onde o cliente envia suas requisições
  client.subscribe("calculadora/solicitacao")

# Callback para quando o servidor receber uma solicitação de cálculo do cliente
def on_message(client, userdata, msg):
  print(f"Mensagem recebida: {msg.payload.decode()}")
  
  # Decodifica a mensagem recebida
  request = json.loads(msg.payload.decode())
  x = request['x']
  y = request['y']

  # Realiza todas as operações e publica os resultados no tópico 'calculadora/resultado'
  resultados = {
      "soma": soma(x, y),
      "subtracao": subtracao(x, y),
      "multiplicacao": multiplicacao(x, y),
      "divisao": divisao(x, y)
  }
    # Publica todos os resultados no tópico 'calculadora/resultado'
  client.publish("calculadora/resultado", json.dumps(resultados))

# Cria o cliente MQTT
client = mqtt.Client()

# Atribuir os callbacks
client.on_connect = on_connect
client.on_message = on_message

# Conectar ao broker MQTT
client.connect("localhost", 1883, 60)

# Iniciar o loop para manter a conexão ativa e processar as mensagens
client.loop_forever()




