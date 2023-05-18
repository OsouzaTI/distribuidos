import json
import constants
from criptografia import *

class ClientData:
    
    def __init__(self, type, name, identifier, message) -> None:
        self.type = type
        self.identifier = identifier
        self.message = message
        self.name = name
    
    @staticmethod
    def fromJson(data):

        # carrega as chaves publica e privada
        privateKey, publicKey = loadKeys()
        decripto_data = rsa.decrypt(data, privateKey).decode()
        print('DECRIPTO: ' + decripto_data)
        
        # Analisa o JSON em uma estrutura de dados Python
        data = json.loads(decripto_data)

        # Inicializa uma nova instância da classe ClientData
        return ClientData(
            type=data['type'],
            name=data['name'],
            identifier=data['identifier'],
            message=data['message']
        )

    def __str__(self) -> str:
        return json.dumps({
            "type": self.type,
            "identifier": str(self.identifier),
            "name": self.name,
            "message": self.message,
        })

