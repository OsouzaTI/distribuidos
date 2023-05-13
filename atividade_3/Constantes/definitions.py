from datetime import datetime


HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 5001         # Porta usada para a comunicação

class ServerLogInfo:
    first = True
    limit = 0
    date = None
    def __init__(self, limit) -> None:
        self.limit = limit
        self.update_date()

    def update_date(self):
        self.date = datetime.now().strftime("%d_%m_%Y_%H_%M")


class ServerConstants:

    CLOSE_CONNECTION = b'CLOSE_CONNECTION'

    def is_close_connection(constant : bytes):
        return constant == ServerConstants.CLOSE_CONNECTION