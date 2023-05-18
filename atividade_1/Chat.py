import socket
import settings
import constants
import uuid
from criptografia import *
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

        # gerando chaves
        generateKeys()
        self.privateKey, self.publicKey = loadKeys()

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
                
                clientData = ClientData.fromJson(data)
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
                    
                    criptografado = rsa.encrypt(str(serverData).encode(), self.publicKey)
                    conn.sendall(criptografado)

                else:                
                    # for chave, valor in self.users.items():
                    #     print(chave, ":", valor)
                    usuario = self.users[f'{identificador}']
                    print(f'[{usuario}]: {clientData.message}')

                    criptografado = rsa.encrypt(str(ServerData.success()).encode(), self.publicKey)
                    conn.sendall(criptografado)
            except Exception as e: 

                print(f'Erro: {e}')
                break

        # Fecha a conexão
        conn.close()


