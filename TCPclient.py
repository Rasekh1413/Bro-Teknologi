from socket import *

serverName = 'localhost'  # eller tilføj en adresse fra anden computer eller server IP
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print(f"Connected to {serverName}:{serverPort}")

try:
    while True:
        command = input("Valg en kommando (Random, Add, Subtract, exit): ").strip()
        if not command:
            continue

        clientSocket.send(command.encode()) # sendes kommando til server

        if command.lower() == "exit":
            print("Exiting client...")
            break

        # modtage server besked
        server_msg = clientSocket.recv(1024).decode().strip()
        print(f"Server: {server_msg}")

        numbers = input("Tilføj tal med mellemrum i midt: ").strip()
        clientSocket.send(numbers.encode())

        # receive result
        result = clientSocket.recv(1024).decode().strip()
        print(f"Resultatet fra serveret: {result}")

finally:
    clientSocket.close()
    print("Forbindelsen er lukket")
