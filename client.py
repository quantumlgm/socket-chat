import socket
import threading

with socket.socket() as client:
    client.connect(('127.0.0.1', 8888))
    client.settimeout(20.0)
    
    user = input('Введите ваше имя: ')
    client.sendall(user.encode('utf-8'))

    while True:
        try:
            text = input('Введите ваше сообщение: ')
            client.sendall(text.encode('utf-8'))
        
        except TimeoutError:
            print('Таймаут со стороны сервера. Соединение закрыто')
            break