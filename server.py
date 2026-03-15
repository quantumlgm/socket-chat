import socket
import threading

with socket.socket() as server:
    server.bind(('127.0.0.1', 8888))
    server.listen(5)
    server.settimeout(20.0)
    print('Сервер создан')

    try:
        while True:
            client, addr = server.accept()
            user = client.recv(1024)
            if not user:
                continue
            user_name = user.decode('utf-8')
            print(f'[Новый клиент]: {addr[0]}, {user_name} ')

            while True:
                try:
                    data = client.recv(1028)
                    if not data:
                        print('Соединение разорвано')
                        break

                    data_decoded = data.decode('utf-8')
                    print(f'{user_name}: {data_decoded}')
                except TimeoutError:
                    break

    except TimeoutError:
        print('Превышено время ожидания')
