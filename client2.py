# client.py
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8080))

    while True:
        message = input("You: ")
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
