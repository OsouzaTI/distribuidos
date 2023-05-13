import socket
import settings
import constants
import uuid
import json
import threading
from ServerData import ServerData
from ClientData import ClientData

class Chat:

    users = {}
    messages = []

    def __init__(self, maxUsers = 5):
        # Cria um objeto socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Associa o objeto socket ao endereço e porta especificados
        self.s.bind((settings.HOST, settings.PORT))
        # Define o limite máximo de conexões simultâneas
        self.s.listen(maxUsers)

        print(f'Servidor escutando na porta {settings.PORT}...')

        while True:

            # Aguarda uma conexão
            conn, addr = self.s.accept()
            print(f'Conectado por {addr}')

            threading.Thread(target=self.run, args=(conn,)).start()


    def run(self, conn):
              
        # esperando conexões
        while True:
            
            try:

                # Aguarda uma mensagem do cliente
                data = conn.recv(1024)
                
                clientData = ClientData.fromJson(data.decode())
                if clientData.type == constants.ClientMessageType.CONNECT:
                    print(str(clientData))
                    
                    # gerando identificador unico desse usuario
                    identificador = uuid.uuid4()
                    print(f'Identificador Criado: {identificador}')
                    self.users[f'{identificador}'] = clientData.name

                    # se for a primeira conexao, enviamos as ultimas mensagens e o proprio identificador                    
                    serverData = ServerData(
                        constants.ServerMessageType.DATA,
                        identificador, 
                        len(self.users),
                        self.messages
                    )

                    conn.sendall(str(serverData).encode())

                else:                
                    # for chave, valor in self.users.items():
                    #     print(chave, ":", valor)
                    usuario = self.users[f'{identificador}']
                    print(f'[{usuario}]: {clientData.message}')
                    conn.sendall(str(ServerData.success()).encode())
            except Exception as e: 

                print(f'Erro: {e}')
                break

        # Fecha a conexão
        conn.close()


