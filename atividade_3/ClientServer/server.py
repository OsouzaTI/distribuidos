import socket
import threading
import psutil
from Constantes.definitions import HOST, PORT
from Constantes.definitions import ServerConstants, ServerLogInfo
from Constantes.helpers import *

class ServerThread:

    threads = {}
    
    def __init__(self, limit = 60) -> None:
        self.limit = limit          
        pass

    # funcao passada a cada conexao multithread
    def handle_client(self, conn, addr, limit, threadId):
        _limit = limit
        """Lida com a conexão de um cliente."""
        with conn:
            print(f'Conexão estabelecida por {addr}')
            serverLogInfo = ServerLogInfo(limit)
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                with open_file_log(threadId, server_info=serverLogInfo) as f:
                    log = f'{get_cpu_usage()};{get_memory_usage()};\n'
                    f.write(log)
                    f.close()              

                # decrementa o limite
                if _limit > 0: 
                    _limit -= 1
                else:
                    break

                reverse = (data.decode())[::-1]
                conn.sendall(reverse.encode())

            # removendo essa thread do mapa
            self.threads.pop(addr[1])
            print(f'threads restantes: {len(self.threads)}')
            if len(self.threads) == 0:  
                print('atualizando horario')
                # se nao houver mais threads, atualize a data
                self.serverLogInfo.update_date()

            conn.sendall(ServerConstants.CLOSE_CONNECTION)   
            print(f'Conexão fechada por {addr}')
    
    # inicia a thread de cada conexão
    def start(self):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # bind o servidor
            s.bind((HOST, PORT))
            s.listen()

            while True:

                if len(self.threads) == 0:
                    print('Esperando conexões...')

                conn, addr = s.accept()
                
                # Cria uma nova thread para lidar com a conexão
                t = threading.Thread(
                    target=self.handle_client,
                    args=(conn, addr, self.limit, len(self.threads))
                )

                # toda conexao aceita sera guardada
                self.threads[addr[1]] = t

                t.start()