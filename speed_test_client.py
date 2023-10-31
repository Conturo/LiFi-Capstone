import socket
import time
from random import randbytes

DATA_SIZE = 1000000

# IP address and port of the server
#server_ip = 'DF-2TK21604MF'  
server_port = 12345 
server_ip = socket.gethostname()



# Connect to the server
outputFile = open("client_results.csv", "w")
outputFile.write("Trial #,Data Transfer Time (ns),Data Size (Bytes),Data Transfer Rate (KB/s)\n")
# Define the data to send
data_to_send = randbytes(DATA_SIZE)

for i in range(50):
    time.sleep(1)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_ip, server_port))
        
    start_time = time.time_ns()  # Record the start time

    # Send the data to the server
    client_socket.send(data_to_send)

    end_time = time.time_ns()  # Record the end time

    # Calculate the transfer time
    transfer_time = end_time - start_time

    # Calculate and print the data transfer rate
    print(f"Data Size: {DATA_SIZE} | Time: {transfer_time}")
    try:
        data_rate = DATA_SIZE / transfer_time*pow(10,9) /1024 # In KB/s
    except:
        data_rate = 0
    outputFile.write(f"{i+1},{transfer_time},{DATA_SIZE},{data_rate}\n")
    
    print(f"Trial {i}: {data_rate} KB/s")
    client_socket.close()
    
outputFile.close()