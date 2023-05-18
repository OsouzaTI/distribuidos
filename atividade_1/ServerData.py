import json
import constants
from criptografia import *

class ServerData:
    
    def __init__(self, type, identifier, usersOnline, lastMessages = [], message = None) -> None:
        self.type = type
        self.identifier = identifier
        self.message = message
        self.usersOnline = usersOnline
        self.lastMessages = lastMessages[-2:]
    
    @staticmethod
    def fromJson(data):

        # carrega as chaves publica e privada
        privateKey, publicKey = loadKeys()
        decripto_data = rsa.decrypt(data, privateKey).decode()

        # Analisa o JSON em uma estrutura de dados Python
        data = json.loads(decripto_data)

        # Inicializa uma nova instância da classe ServerData
        return ServerData(
            type=data['type'], 
            identifier=data['identifier'],
            usersOnline=data['usersOnline'],
            lastMessages=data['lastMessages'],
            message=data['message']
        )

    @staticmethod
    def success():
        
        # Inicializa uma nova instância da classe ServerData
        return ServerData(
            type=constants.ClientMessageType.INVALID, 
            identifier=constants.ClientMessageType.INVALID,
            usersOnline=constants.ClientMessageType.INVALID,
            lastMessages=[],
            message=constants.ClientMessageType.INVALID
        )

    def __str__(self) -> str:
        return json.dumps({
            "type": self.type,
            "identifier": str(self.identifier),
            "lastMessages": self.lastMessages,
            "message": self.message,
            "usersOnline": self.usersOnline
        })

