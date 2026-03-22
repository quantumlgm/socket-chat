import socket
import threading

lock = threading.Lock()
clients = []

def client_processing(client_socket, address):
    user_name = ""
    try:
        data = client_socket.recv(1024)
        if not data:
            return
        user_name = data.decode('utf-8')
        
        with lock:
            clients.append((client_socket, user_name))
        
        print(f'[НОВОЕ ПОДКЛЮЧЕНИЕ]: {address[0]} зашел как "{user_name}"')
        broadcast(f"Система: {user_name} присоединился к чату", client_socket)

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            message = data.decode('utf-8')
            full_message = f"{user_name}: {message}"
            print(full_message)
            broadcast(full_message, client_socket)

    except (ConnectionResetError, BrokenPipeError):
        pass
    finally:
        with lock:
            for c in clients:
                if c[0] == client_socket:
                    clients.remove(c)
                    break
        client_socket.close()
        if user_name:
            print(f"[ОТКЛЮЧЕНИЕ]: {user_name} покинул чат.")
            broadcast(f"Система: {user_name} покинул чат", None)

def broadcast(message, sender_socket):
    with lock:
        for client, _ in clients:
            if client != sender_socket:
                try:
                    client.sendall(message.encode('utf-8'))
                except:
                    client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('127.0.0.1', 8888))
        server.listen(5)
        print('--- Сервер запущен и ожидает сообщений ---')
        
        while True:
            client_socket, addr = server.accept()
            thread = threading.Thread(target=client_processing, args=(client_socket, addr))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server.close()

if __name__ == "__main__":
    main()