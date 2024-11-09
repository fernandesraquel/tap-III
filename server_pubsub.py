# Importando a biblioteca paho.mqtt.client para trabalhar com o protocolo MQTT 
# e a biblioteca json para manipulação de dados JSON
import paho.mqtt.client as mqtt
import json

# Funções da calculadora
def soma(x, y): return x + y 

def subtracao(x, y): return x - y 

def multiplicacao(x, y): return x * y  

def divisao(x, y): return x / y if y != 0 else "Erro: divisão por zero"  

# Callback executado quando o cliente se conecta ao servidor MQTT (broker)
def on_connect(client, userdata, flags, reason_code, props):
    print("Inscrevendo-se em calculadora...")  # Exibe uma mensagem quando a conexão for bem-sucedida
    client.subscribe("calculadora/solicitacao")  # Inscreve-se no tópico 'calculadora/solicitacao', onde as solicitações de cálculos serão publicadas

# Callback executado quando uma mensagem é recebida de um tópico ao qual o cliente está inscrito
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))  # Exibe o tópico e a mensagem recebida

    # Decodifica a mensagem recebida, que está em formato JSON
    request = json.loads(msg.payload.decode())  
    x = request['x']  # Obtém o valor de x da mensagem recebida
    y = request['y']  # Obtém o valor de y da mensagem recebida

    # Calcula os resultados das operações e os armazena em um dicionário
    resultados = {
        "soma": soma(x, y),
        "subtracao": subtracao(x, y),
        "multiplicacao": multiplicacao(x, y),
        "divisao": divisao(x, y)
    }

    # Publica os resultados das operações no tópico 'calculadora/resultado'
    client.publish("calculadora/resultado", json.dumps(resultados))  # Envia os resultados em formato JSON para o tópico de resultados

# Cria um cliente MQTT e configura a versão da API de callback
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Define as funções de callback para conexão e recebimento de mensagens
client.on_connect = on_connect
client.on_message = on_message

# Conecta o cliente ao broker MQTT na máquina local na porta 1883 com o tempo limite de 60 segundos
client.connect("localhost", 1883, 60)

# Chamada bloqueante que inicia o loop para processar tráfego de rede, despachar callbacks e lidar com reconexões
client.loop_forever()


