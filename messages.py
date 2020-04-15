import socket

def message_reader() -> None:
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 12000

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))

        while True:
            try:
                server_msg = socket_instance.recv(1024)
                print(server_msg.decode())
            except Exception as e:
                print(f'Error handling server messages, closing conection: {e}')
                socket_instance.close()


        socket_instance.close()

    except Exception as e:
        print(f'Error connecting to server socket {e}')


if __name__ == "__main__":
    message_reader()