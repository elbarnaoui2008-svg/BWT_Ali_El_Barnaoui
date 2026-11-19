import socket

def bwt(S):
    lista = []

    for i in range(len(S) + 1):
        s = S[i:] + "$" + S[:i]
        lista.append(s)

        lista.sort()
        S_finale = ""

        for i in range(len(lista)):
            S_finale = S_finale + (lista[i][-1])

        return S_finale


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("127.0.0.1", 5000))
    server.listen()
    print("Server in ascolto...")

    conn, addr = server.accept()

    with conn:
        print("Client connesso:", addr)

        # 1. Riceve i byte dal client e li trasforma in stringa con .decode()
        S = conn.recv(1024).decode()
        print("Parola ricevuta dal client:", S)

        # 2. Elabora la trasformata usando la tua funzione
        S_finale = bwt(S)
        print("Trasformata calcolata:", S_finale)

        # 3. Ritrasforma il risultato in byte con .encode() e lo invia al client
        conn.sendall(S_finale.encode())