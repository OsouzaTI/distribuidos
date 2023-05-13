import socket

HOST = ''  # Endereço IP do servidor
PORT = 5002  # Porta que o servidor vai escutar

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o objeto socket ao endereço e porta especificados
s.bind((HOST, PORT))

# Define o limite máximo de conexões simultâneas
s.listen(1)

print(f'Servidor escutando na porta {PORT}...')

# Aguarda uma conexão
conn, addr = s.accept()
print(f'Conectado por {addr}')

while True:

    try:
        # Aguarda uma mensagem do cliente
        data = conn.recv(1024)
        print(f'Mensagem recebida: {data.decode()}')

        # Envia uma resposta para o cliente
        conn.sendall('Mensagem recebida com sucesso!'.encode())

    except:

        print('Servidor encerrado!!!')
        break
 

# Fecha a conexão
conn.close()
