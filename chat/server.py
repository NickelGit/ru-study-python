import socket
import logging
from settings import (
    HOST,
    PORT,
    MESSAGE_LOG_MAX_LEN,
    EXIT_COMMAND,
    TIMESTAMP_FORMAT,
    ENCODING_FORMAT,
    CHATBOT_NAME,
)
from threading import Thread
from datetime import datetime

connected_users: dict = {}
messages_log: list = []
sending_queue: list = []


def format_message(user_name: str, text: str) -> str:
    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    return f"[{timestamp}]--{user_name}--: {text}"


def add_message_to_log(message: str) -> None:
    if len(messages_log) > MESSAGE_LOG_MAX_LEN:
        messages_log.pop(0)

    messages_log.append(message)


def add_to_sending_queque(message: str, author_name: str) -> None:
    sending_queue.append({"text": message, "author": author_name})


def send_greeting_message(user_name: str) -> None:
    message_text = f"Hooray! {user_name} joined the chat!"
    formatted_message = format_message(CHATBOT_NAME, message_text)
    add_to_sending_queque(formatted_message, CHATBOT_NAME)
    logging.info(formatted_message)


def send_farewell_message(user_name: str) -> None:
    message_text = f"Bye-bye! {user_name} left the chat!"
    formatted_message = format_message(CHATBOT_NAME, message_text)
    add_to_sending_queque(formatted_message, CHATBOT_NAME)
    logging.info(formatted_message)


def send_message_to_active_clients(message: tuple) -> None:
    for user_name in connected_users:
        if user_name == message["author"]:
            continue

        user = connected_users[user_name]
        connection = user["connection"]
        connection.sendall(bytes(message["text"], ENCODING_FORMAT))


def send_messages_from_queue() -> None:
    while True:
        if sending_queue:
            message = sending_queue[0]
            send_message_to_active_clients(message)
            sending_queue.pop(0)


def messages_log_multistring() -> str:
    return "\n".join([message for message in messages_log])


def connect_user(ip: str, port: str, name: str, connection: socket.socket) -> None:
    connected_users[name] = {"ip": ip, "port": port, "connection": connection}


def disconnect_user(user_name: str, connection: socket.socket) -> None:
    del connected_users[user_name]
    connection.close()


def receive_data(connection: socket.socket) -> str:
    return connection.recv(1024).decode(ENCODING_FORMAT)


def new_client(connection: socket.socket) -> None:
    with connection:
        ip, port = connection.getpeername()
        name = receive_data(connection)
        connect_user(ip, port, name, connection)

        connection.sendall(bytes(messages_log_multistring(), ENCODING_FORMAT))
        send_greeting_message(name)

        while True:
            try:
                data = receive_data(connection)
            except OSError:
                break

            if data == EXIT_COMMAND or not data:
                disconnect_user(name, connection)
                send_farewell_message(name)
            else:
                formatted_message = format_message(name, data)
                logging.info(f"{ip}:{port} - {formatted_message}")
                add_message_to_log(formatted_message)
                add_to_sending_queque(formatted_message, name)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    logging.basicConfig(level=logging.INFO)
    s.bind((HOST, PORT))
    s.listen()
    Thread(target=send_messages_from_queue, args=()).start()
    while True:
        conn, addr = s.accept()
        Thread(target=new_client, args=(conn,)).start()
