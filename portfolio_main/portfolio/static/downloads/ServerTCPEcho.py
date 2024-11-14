'''Michael Jolley - Socket Programming Project - ServerTCPEcho'''

import socket
import time
import signal
import sys

# Function to handle server shutdown without causing errors
def signal_handler(sig, frame):
    print('\nServer shutting down...')
    sys.exit(0)

def return_expression(expression):
    return_value = expression

def server():
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)

    # Take the port number as a command-line argument
    port = int(input("Enter the port number to listen on: "))

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # Bind the socket to the port
        client.bind(('', port))

        # Listen for incoming connections
        client.listen()
        print(f"Server is listening on port {port}")

        while True:
            # Accept a connection
            conn, addr = client.accept()
            with conn:
                print(f"Connected by {addr}")

                while True:
                    # Receive data from the client
                    data = conn.recv(1024).decode()
                    if not data:
                        break

                    # Evaluate the expression
                    result = return_expression()

                    # Reply with the result and the current time
                    reply = f"Echo = {result}, Message Received at {time.ctime()}, thank you!\n"
                    conn.sendall(reply.encode())

                print(f"Connection with {addr} closed")

if __name__ == "__main__":
    server()
