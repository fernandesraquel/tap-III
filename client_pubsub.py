import paho.mqtt.client as mqtt
import json

# Callback para quando o cliente se conectar ao broker
def on_connect(client, obj, flags, reason_code, properties):
  # Após a conexão, o cliente envia os números para o servidor calcular todas as operações
  x = float(input("Informe o primeiro número: "))
  y = float(input("Informe o segundo número: "))

  # Criar uma mensagem com os números para o servidor calcular
  mensagem = json.dumps({"x": x, "y": y})
  
  # Publica a solicitação no tópico 'calculadora/solicitacao'
  client.publish("calculadora/solicitacao", mensagem)

  # Inscreve-se no tópico de resultados para receber todas as operações
  client.subscribe("calculadora/resultado")

# Callback para quando o cliente receber a resposta do servidor
def on_message(client, userdata, msg):
  resultados = json.loads(msg.payload.decode())
  print("Resultados recebidos:")
  print(f"Soma: {resultados['soma']}")
  print(f"Subtração: {resultados['subtracao']}")
  print(f"Multiplicação: {resultados['multiplicacao']}")
  print(f"Divisão: {resultados['divisao']}")

# Cria o cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.on_connect = on_connect

# Conecta ao broker MQTT
client.connect("localhost", 1883, 60)

# Inicia o loop para manter a conexão ativa e processar as mensagens
client.loop_forever()

