S = input("Scrivi la parola a qui applicare il BWT")

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

    S_finale = bwt(S)
    print(S_finale)