import socket
import threading

server = ('127.0.0.1', 9099)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(('', 0))
client.connect(server)


def read_sock():
    while True:
        data = client.recv(1024)
        print(f'{data.decode("utf-8")}')


nickname = input('\nEnter nickname: ')
client.send(nickname.encode('utf-8'))
thr1 = threading.Thread(target=read_sock)
thr1.start()

while True:
    mess = input(f'{nickname}: ')
    client.send(mess.encode('utf-8'))
