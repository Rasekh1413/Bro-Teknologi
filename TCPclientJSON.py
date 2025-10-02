from socket import *
import json
# TCP Python client som JSON. Du kan bruge og køre en af Server med JSON python til at teste denne TCP client.
# bruge denne eksempler for at teste: random, add, subtract, exit. Det er jo samme som Klient, men det konverter til JSON til serveret {"method": "Random", "Tal1": 10, "Tal2": 20}
serverName = 'localhost'
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print(f"Klientet er klar med JSON til at kører og er forbinde med: {serverName}:{serverPort}")

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

        # Sendes JSON til server og Konvertere til to JSON
        json_string = json.dumps(request)

        # Printes JSON som er sentet
        print(f"Sending JSON to server: {json_string}")

        clientSocket.send((json_string + "\n").encode())
        if command.lower() == "exit":
            print("Klient lukker...")
            break

        # modtage server svaret
        response_data = clientSocket.recv(1024).decode().strip()
        try:
            response = json.loads(response_data)
            print(f"Resultatet fra serveret: {response.get('result')}")
        except json.JSONDecodeError:
            print(f"Server svar: {response_data}")

finally:
    clientSocket.close()
    print("Forbindelsen er lukket")
