import socket
import json
import settings, constants
from Chat import Chat
from ClientData import ClientData
from ServerData import ServerData

class User:

    # objeto de conexão
    s = None
    identifier = None

    def __init__(self, nome) -> None:
        self.nome = nome
        self.connect()

    def connect(self) -> None:
        # Cria um objeto socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conecta ao servidor
        self.s.connect((settings.HOST, settings.PORT))

        # conexao do cliente
        self.send(str(ClientData(constants.ClientMessageType.CONNECT, self.nome, None, None)))

        # processo de mensgens
        self.mensage()

    def mensage(self):
        
        # esperando mensagem
        while True:
            msg = input(f'[{self.nome}]: ')
            self.send(str(ClientData(constants.ClientMessageType.DATA, self.nome, self.identifier, msg)))

    def send(self, message):
        # Envia uma mensagem para o servidor
        self.s.sendall(message.encode())
        # esperando resposta do servidor
        resposta = self.s.recv(1024)
        
        serverData = ServerData.fromJson(resposta.decode())
        
        if self.identifier == None:
            self.identifier = serverData.identifier

nome = input("Digite seu nome: ")
u = User(nome)