import paho.mqtt.client as mqtt
import time

BROKER = "192.168.0.112"  # Altere para o IP do seu broker
TOPICO = "teste"
PORT = 1890

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado com sucesso ao broker!")
    else:
        print(f"❌ Falha ao conectar. Código: {rc}")

def on_publish(client, userdata, mid):
    print(f"Mensagem publicada com sucesso! ID de mensagem: {mid}")

cliente = mqtt.Client()
cliente.on_connect = on_connect
cliente.on_publish = on_publish

try:
    cliente.connect(BROKER, PORT, 60)
    cliente.loop_start()

    time.sleep(1)  # Espera a conexão estabilizar

    movimento = input("Digite o movimento para enviar: ")
    result = cliente.publish(TOPICO, movimento, qos=1)
    print(f"Resultado da publicação: {result.rc}")

    cliente.disconnect()

except Exception as e:
    print(f"Erro ao conectar ou publicar: {e}")
