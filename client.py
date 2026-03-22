import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("\n[Связь с сервером потеряна]")
                break

            sys.stdout.write('\r' + ' ' * 50 + '\r') 
            print(message)
            sys.stdout.write("Вы: ")
            sys.stdout.flush()
        except:
            break

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 8888))
        
        name = input('Введите ваше имя: ').strip()
        if not name:
            name = "Anonymous"
        client.sendall(name.encode('utf-8'))


        thread = threading.Thread(target=receive_messages, args=(client,))
        thread.daemon = True
        thread.start()

        print("--- Вы вошли в чат (пишите 'exit' для выхода) ---")
        
        while True:
            msg = input("Вы: ")
            
            if msg.lower() == 'exit':
                break
            
            if msg.strip():
                client.sendall(msg.encode('utf-8'))

    except ConnectionRefusedError:
        print('Ошибка: Сервер не найден.')
    except Exception as e:
        print(f'Ошибка: {e}')
    finally:
        client.close()
        print("Сессия завершена.")

if __name__ == "__main__":
    main()