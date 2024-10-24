'''Michael Jolley - Socket Programming Project - ClientTCPEcho'''

import socket

def client():
    # Take server hostname and port number as command-line arguments
    hostname = input("Enter server hostname (localhost or IP address): ")
    port = int(input("Enter server port number: "))

    # Create a TCP socket socket.AF_INET is the family and socket.SOCK_STREAM is the type of connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Connect to the server
        server.connect((hostname, port))

        # Print the IP address and port of the server connected to
        print(f"Connected to server {hostname}:{port}")

        while True:
            # Ask the user for a message to send and takes into account the sentinel value if given to exit the code
            message = input("Enter a message to send to the server. ('Exit' to exit): ")
            # Break if key sentinel is given
            if message == 'Exit':
                break

            # Send the message to the server, use send all to send all your dad buffer will call socket.send() until the entire message is sent
            server.sendall(message.encode())

            # Read the answer from the server
            data = server.recv(1024)

            # Display the answer to the user by decoding the message then displaying it
            print(f"Received from server: {data.decode()}")

        # Close the connection to the server
        print("Closing connection to server...")
        server.close()

if __name__ == "__main__":
    client()
