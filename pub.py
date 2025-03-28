import paho.mqtt.client as mqtt

# Configuração do MQTT
BROKER = "192.168.0.112"  # Altere para o IP do seu broker
TOPICO = "teste"
PORT = 1885

# Criando o cliente MQTT
cliente = mqtt.Client()
cliente.connect(BROKER, PORT, 60)

# Movimento de exemplo (e2e4 é um lance inicial comum no xadrez)
movimento = input("Digite aqui: ")

# Publica o movimento
cliente.publish(TOPICO, movimento)
print(f"Movimento '{movimento}' enviado para o tópico '{TOPICO}'")

# Desconecta após publicar
cliente.disconnect()
