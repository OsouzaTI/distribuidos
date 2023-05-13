import socket
from time import sleep

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5002  # Porta do servidor

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor
s.connect((HOST, PORT))

for i in range(10):
    print(f'Dado {i} enviado.')
    # Envia uma mensagem para o servidor
    s.sendall('Olá, servidor!'.encode())

    # Aguarda uma resposta do servidor
    data = s.recv(1024)

    # Imprime a resposta recebida
    print(f'Resposta do servidor: {data.decode()}')
    sleep(2)

# Fecha a conexão
s.close()
