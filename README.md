# MQTT-Last Will e Retain Flag
Implementação simples dos conceitos de LWT e Retain Flag

# O que é e como funciona:
Last Will (LWT): É a "última vontade" do dispositivo. Uma mensagem pré-definida que o Broker guarda assim que o cliente se conecta. O cliente envia os detalhes do LWT (tópico e mensagem) no pacote CONNECT. O Broker monitora a conexão. Se o cliente desconectar de forma abrupta (perda de sinal ou falta de Keep Alive), o Broker publica essa mensagem automaticamente para os interessados. Se o cliente desconectar normalmente (comando DISCONNECT), o Broker descarta a mensagem.

Retain Flag: É um marcador que transforma uma mensagem comum em uma "mensagem persistente" no Broker. Quando você publica com retain=True, o Broker armazena essa mensagem e seu respectivo tópico em memória. Sempre que um novo cliente se inscrever (Subscribe) naquele tópico, o Broker envia a mensagem retida imediatamente, mesmo que o dispositivo que a enviou esteja offline no momento.

# Quando usar cada um:
Last Will (LWT): Use exclusivamente para notificar desconexão. É configurado na conexão para que o Broker avise os outros quando o dispositivo "morrer" subitamente.

Retain Flag: Use para armazenar o último estado. Serve para que qualquer novo cliente que se conectar ao tópico receba o valor atual imediatamente, sem esperar uma nova transmissão.

# Impactos no sistema IoT real:
Last Will (LWT): Evita a leitura de dados falsos ou defasados. Se um sensor de temperatura trava, o sistema sabe instantaneamente que o dispositivo está offline e invalida os dados anteriores.

Retain Flag: Garante a persistência do estado. Se uma lâmpada inteligente é reiniciada ou um novo celular abre o aplicativo, o estado (Ligado/Desligado) é recuperado na hora do Broker.
