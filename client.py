import socket, select, sys, threading

def handle_server_messages(socket: socket.socket) -> None:
    while True:
        try:
            server_msg = socket.recv(1024)
            print(server_msg.decode())
        except Exception as e:
            print(f'Error handling server messages, closing conection: {e}')
            socket.close()

def client() -> None:
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000
    
    open_thread = None

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))

        while True:
            if not open_thread:
                open_thread = threading.Thread(target=handle_server_messages, args=(socket_instance))

            msg = input('Insert a message: ')

            if msg == 'quit':
                break

            socket_instance.send(msg.encode())

        socket_instance.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')


if __name__ == "__main__":
    client()