import socket
import time

# server IP and port
server_ip = '192.168.1.2'
server_port = 12345
server_ip = socket.gethostname()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))

server_socket.listen(5)

print(f"\nServer is listening on {server_ip}:{server_port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    start_time = time.time_ns()  # Record the start time

    # Receive data from the client
    #received_data = client_socket.recv(1024)
    print(received_data)

    end_time = time.time_ns()  # Record the end time

    # Calculate the transfer time
    transfer_time = end_time - start_time
    print(f"Data transfer time: {transfer_time:.4f} nanoseconds")

    # Calculate and print the data transfer rate
    data_rate = float(len(received_data)) / transfer_time / 1024.0  # In KB/s
    print(f"Data transfer rate: {data_rate:.2f} KB/s")

    # Close the client socket
    client_socket.close()
