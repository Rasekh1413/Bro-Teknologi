from socket import *
import json

serverName = 'localhost'
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print(f"Connected to {serverName}:{serverPort}")

try:
    while True:
        command = input("Valg en kommando (Random, Add, Subtract, exit): ").strip()
        if not command:
            continue

        # den er med JSON format
        request = {"method": command}
        if command.lower() != "exit":
            numbers = input("tilføj tal med mellemrum: ").strip()
            try:
                tal1, tal2 = map(int, numbers.split())
                request["Tal1"] = tal1
                request["Tal2"] = tal2
            except:
                print("Forkerte tal, prøv igen.")
                continue

        # Sendes JSON til server
        clientSocket.send((json.dumps(request) + "\n").encode())

        if command.lower() == "exit":
            print("Klient lukker...")
            break

        # motage server svar
        response_data = clientSocket.recv(1024).decode().strip()
        try:
            response = json.loads(response_data)
            print(f"Resultatet fra serveren: {response.get('result')}")
        except json.JSONDecodeError:
            print(f"Server svar: {response_data}")

finally:
    clientSocket.close()
    print("Forbindelsen er lukket")
