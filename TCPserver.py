#
from socket import *
import random
# TCP Python server, bruge sockettest til at teste.
# bruge denne eksempler for at teste: random, add, subtract, exit
serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(33) # Så kan 33 servere køres samtidigt :)
print('Serveret er klar til at modtage som JSON scripter')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"forbindleet til: {addr}")

    while True:
        command = connectionSocket.recv(1024).decode().strip()
        if not command or command.lower() == 'exit':
            print("modtaget exit kommando, lukker forbindelsen")
            break

        connectionSocket.send("input numbers\n".encode()) # denne \n hjælper til næste linje

        data = connectionSocket.recv(1024).decode().strip()
        tal1, tal2 = map(int, data.split())

        if command == "random":
                result = random.randint(tal1, tal2)
        elif command == "add":
                result = tal1 + tal2
        elif command == "subtract":
                result = tal1 - tal2
        # Vigtig: Jeg ved ikke hvorfor når jeg skriver else for det sidte, giver det en fejl efter command?

        connectionSocket.send(str(f"{result}\n").encode()) # denne \n hjælper til næste linje, og result skal inde {}.

    connectionSocket.close()
    print("Connectionen er lukket")