import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Edis Protocol Initialized....")

if __name__ == "__main__":
    start_server()
