# server.py
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))
    server_socket.listen(1)

    print("Server is listening on port 8080...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")
        message = input("You: ")
        conn.sendall(message.encode())

    conn.close()

if __name__ == "__main__":
    start_server()
