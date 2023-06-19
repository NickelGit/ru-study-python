import socket
from threading import Thread
from settings import HOST, PORT, ENCODING_FORMAT, EXIT_COMMAND


def receive_messages(connection: socket.socket) -> None:
    while True:
        try:
            data = connection.recv(1024).decode(ENCODING_FORMAT)
            if data:
                print(data)
        except (ConnectionResetError, BrokenPipeError, OSError):
            break


def exit_chat(connection: socket.socket) -> None:
    connection.close()
    exit()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    nickname = input("Enter your nickname: ")
    s.sendall(bytes(nickname, ENCODING_FORMAT))

    Thread(target=receive_messages, args=(s,)).start()

    while True:
        send_data = input()
        try:
            s.sendall(bytes(send_data, ENCODING_FORMAT))
        except (ConnectionResetError, BrokenPipeError, OSError):
            break

        if send_data == EXIT_COMMAND:
            exit_chat(s)
            break
