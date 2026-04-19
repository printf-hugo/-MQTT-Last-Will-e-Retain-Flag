import paho.mqtt.client as mqtt
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(name)

BROKER = "mqtt.eclipseprojects.io"
PORTA = 1883
TOPICO_STATUS = "projeto/dispositivo_01/status"
TOPICO_TELEMETRIA = "projeto/dispositivo_01/temperatura"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Conectado ao Broker com sucesso.")
        # RETAIN: Garante que qualquer um que se conectar saiba que o status é ONLINE
        client.publish(TOPICO_STATUS, "ONLINE", qos=1, retain=True)
    else:
        logger.error(f"Falha na conexão. Código: {rc}")

def configurar_cliente():
    client = mqtt.Client("ESP32_Simulado_01")

    client.will_set(TOPICO_STATUS, payload="OFFLINE", qos=1, retain=True)

    client.on_connect = on_connect
    return client

def executar_dispositivo():
    client = configurar_cliente()

    try:
        client.connect(BROKER, PORTA, keepalive=60)
        client.loop_start()

        while True:
            valor_temp = "26.5"
            # RETAIN: O último valor de temperatura fica salvo no Broker
            client.publish(TOPICO_TELEMETRIA, payload=valor_temp, qos=1, retain=True)
            logger.info(f"Dados enviados: {valor_temp}°C (Retain=True)")
            time.sleep(10)

    except KeyboardInterrupt:
        logger.warning("\nEncerrando de forma limpa...")
        # Ao sair via Ctrl+C, limpamos o status para OFFLINE manualmente
        client.publish(TOPICO_STATUS, "OFFLINE", retain=True)
        client.disconnect()
    except Exception as e:
        logger.error(f"Erro crítico: {e}")
    finally:
        client.loop_stop()

if name == "main":
    executar_dispositivo() 
