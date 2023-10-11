import socket
import time
from random import randbytes

# IP address and port of the server
#server_ip = '192.168.1.2'  
server_port = 12345 
server_ip = socket.gethostname()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Define the data to send
data_to_send = randbytes(1000)

try:
    start_time = time.time()  # Record the start time

    # Send the data to the server
    #client_socket.send(data_to_send)
    print(data_to_send)

    end_time = time.time()  # Record the end time

    # Calculate the transfer time
    transfer_time = end_time - start_time
    print(f"Data transfer time: {transfer_time:.4f} seconds")

    # Calculate and print the data transfer rate
    data_rate = len(data_to_send) / transfer_time / 1024  # In KB/s
    print(f"Data transfer rate: {data_rate:.2f} KB/s")

finally:
    client_socket.close()
