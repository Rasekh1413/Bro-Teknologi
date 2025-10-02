from socket import *
import random
import json
# TCP Python server som JSON.
# bruge denne eksempler for at teste: {"method": "Random", "Tal1": 10, "Tal2": 20}
# add {"method": "Add", "Tal1": 10, "Tal2": 20}
# subtract {"method": "Subtract", "Tal1": 5, "Tal2": 1}
# exit {"method": "exit"}  <- jeg tror den skal lukkes, men den virker ikke. altså det er jo som method tinker jeg.
serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(33)  # # Så kan 33 servere køres samtidigt :)
print('Serveret er klar til at modtage')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Forbindelse til: {addr}")

    while True:
        try:
            data = connectionSocket.recv(1024).decode().strip()
            if not data or data.lower() == 'exit': # <- den virker ikke, og jeg skal nok søger på det...
                print("Modtaget exit kommando, lukker forbindelsen")
                break

            request = json.loads(data)  # <- den læser JSON
            command = request.get("method", "").lower()
            tal1 = int(request.get("Tal1", 0))
            tal2 = int(request.get("Tal2", 0))

            # såden er kommandene
            if command == "random":
                result = random.randint(tal1, tal2)
            elif command == "add":
                result = tal1 + tal2
            elif command == "subtract":
                result = tal1 - tal2

            # svares som JSON
            response = {"result": result}
            connectionSocket.send((json.dumps(response) + "\n").encode())  # denne \n hjælper til næste linje

        except json.JSONDecodeError:
            connectionSocket.send("Fejl i JSON format\n".encode())
        except Exception as e:
            connectionSocket.send(f"Server fejl: {e}\n".encode())  # denne \n hjælper til næste linje

    connectionSocket.close()
    print("Connectionen er lukket")
