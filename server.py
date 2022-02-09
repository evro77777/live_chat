import socket
import threading

host = '127.0.0.1'
port = 9099

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10)

clients = []
nicknames = []

print('start_server')


def broadcast(message, exception_client=None):
    for client in clients:
        if client == exception_client:
            continue
        else:
            client.send(message)


def handle(client):
    flag_for_nickname = True
    while True:
        try:
            message = client.recv(1024)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            mess = f'{nickname} отключился от сервера\n'
            print(mess)
            broadcast(mess.encode('utf-8'), client)
            nicknames.remove(nickname)
            break
        else:
            if flag_for_nickname:
                flag_for_nickname = False
                nickname = message.decode('utf-8')
                nicknames.append(nickname)
                mess = f'\n{nickname} подключился к серверу'
                print(mess)
                broadcast(mess.encode('utf-8'))
            else:
                index = clients.index(client)
                nickname = nicknames[index]
                mess = f'\n{nickname}:{message.decode("utf-8")}'
                broadcast(mess.encode('utf-8'), exception_client=client)


def receive():
    while True:
        client, addr = server.accept()
        clients.append(client)
        thr = threading.Thread(target=handle, args=(client,))
        thr.start()


receive()

