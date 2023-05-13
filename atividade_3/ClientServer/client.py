import socket
import time
from threading import Thread
from Constantes.definitions import HOST, PORT, ServerConstants
class Client(Thread):

    def __init__(self, delay = 0) -> None:
        super().__init__()
        self.delay = delay

    def run(self):

        # Cria o objeto socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Conecta ao servidor
            s.connect((HOST, PORT))

            while True:
                # Envia uma mensagem para o servidor
                s.sendall(b'Hello World!!!')
                # Recebe a resposta do servidor
                data = s.recv(1024)

                # Exibe a resposta do servidor                
                if ServerConstants.is_close_connection(data):
                    print('conexão encerrada')
                    break

                # controle de tempo de envio
                if self.delay != 0:
                    time.sleep(self.delay)
