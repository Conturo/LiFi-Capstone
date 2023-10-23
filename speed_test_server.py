import socket
import time

# server IP and port
#server_ip = '192.168.1.2'

DATA_SIZE = 1000000

server_port = 12345
server_ip = socket.gethostname()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

outputFile = open("server_results.csv", "a")
outputFile.write("Trial #,Data Transfer Time (ns),Data Size (Bytes),Data Transfer Rate (KB/s)")


for i in range(50):
    server_socket.bind((server_ip, server_port))

    server_socket.listen()
    client_socket, client_address = server_socket.accept()
    
    print(f"Accepted connection for trial #{i+1}")
    
    start_time = time.time_ns()  # Record the start time

    # Receive data from the client
    received_data = client_socket.recv(DATA_SIZE)

    end_time = time.time_ns()  # Record the end time

    # Calculate the transfer time
    transfer_time = end_time - start_time
    
    # Calculate and print the data transfer rate
    data_rate = float(len(received_data)) / transfer_time*pow(10,9) /1024 # In KB/s
    
    outputFile.write(f"{i+1},{transfer_time},{DATA_SIZE},{data_rate}\n")
    
    # Close the client socket
    server_socket.close()

outputFile.close()