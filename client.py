import socket
import threading

server = ('127.0.0.1', 9099)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))


def read_sock():
    while True:
        data = sock.recv(1024)
        print(f'{data.decode("utf-8")}')


def run():
    nickname = input('Enter nickname: ')
    sock.sendto(nickname.encode('utf-8'), server)
    thrd = threading.Thread(target=read_sock)
    thrd.start()
    while True:
        message = input(f'{nickname}: ')
        sock.sendto(message.encode('utf-8'), server)


run()
