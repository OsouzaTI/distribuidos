from ClientServer.client import Client


N_CLIENTS = 100

clients : list[Client] = []

for i in range(N_CLIENTS):
    clients.append(Client())

for c in clients:
    c.start()