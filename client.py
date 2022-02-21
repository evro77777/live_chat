import socket
import threading

server = ('127.0.0.1', 9099)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(('', 0))
client.connect(server)

nickname = input('\nEnter nickname: ')
client.send(nickname.encode('utf-8'))


def read_sock():
    global nickname
    flag = False
    while True:
        data = client.recv(1024).decode('utf-8')
        # in case if the nickname is already in the nicknames
        if data == 'Try again.\n':
            flag = True
            print(f'{data}')
            nickname = 'Enter nickname'
        elif 'nickname=' in data and flag:
            nickname = data.split('=')[-1]
        else:
            print(f'{data}')


thr1 = threading.Thread(target=read_sock)
thr1.start()

while True:
    mess = input(f'{nickname}: ')
    client.send(mess.encode('utf-8'))
