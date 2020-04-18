import socket

def client() -> None:
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))

        while True:
            msg = input('Insert a message: ')

            if msg == 'quit':
                break

            socket_instance.send(msg.encode())

        socket_instance.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')


if __name__ == "__main__":
    client()
