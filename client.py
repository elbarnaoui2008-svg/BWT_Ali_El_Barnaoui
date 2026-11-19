import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("127.0.0.1", 5000))
    S = input("Scrivi la parola a cui applicare l'Algoritmo di Burrows - Wheeler: ")
    client.sendall(S.encode())

    S_finale = client.recv(1024).decode()
    print("Trasformata BWT:", S_finale)