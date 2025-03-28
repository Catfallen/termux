import paho.mqtt.client as mqtt

# Configuração do MQTT
BROKER = "192.168.0.112"  # Altere para o IP do seu broker
TOPICO = "teste"
PORT = 1890

# Callback para confirmar publicação
def on_publish(client, userdata, mid):
    print(f"✅ Movimento '{movimento}' enviado com sucesso para o tópico '{TOPICO}'")

# Criando o cliente MQTT
cliente = mqtt.Client()
cliente.on_publish = on_publish  # Vincula a função de confirmação

# Conectar ao broker
cliente.connect(BROKER, PORT, 60)

# Movimento de exemplo (e2e4 é um lance inicial comum no xadrez)
movimento = input("Digite aqui: ")

# Publica o movimento e obtém um resultado
res = cliente.publish(TOPICO, movimento)

# Aguarda confirmação de envio
res.wait_for_publish()

# Desconecta após publicar
cliente.disconnect()
