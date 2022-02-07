import socket

HOST = '127.0.0.1'
PORT = 9099
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

clients = set()

print('Start server')


def broadcast(message, address):
    for item in clients:
        if item[1] == address:
            continue
        else:
            sock.sendto(message.encode('utf-8'), item[1])


def receive():
    while True:
        data, address = sock.recvfrom(1024)
        flag = True
        for item in clients:
            if address == item[1]:
                nickname = item[0]
                m = f'{nickname}:{data.decode("utf-8")}'
                broadcast(m, address)
                flag = False
                break
            else:
                continue
        if len(clients) == 0 or flag:
            clients.add((data.decode('utf-8'), address))
            m = f'\n{data.decode("utf-8")} подключился к серверу'
            print(m)
            sock.sendto('Вы подключились к серверу'.encode('utf-8'), address)
            broadcast(m, address)


receive()
