"""


 █████╗ ██╗     ██████╗ ██████╗ ██╗ ██████╗ ██╗   ██╗███████╗
██╔══██╗██║     ██╔══██╗██╔══██╗██║██╔════╝ ██║   ██║╚══███╔╝
███████║██║     ██║  ██║██████╔╝██║██║  ███╗██║   ██║  ███╔╝ 
██╔══██║██║     ██║  ██║██╔══██╗██║██║   ██║██║   ██║ ███╔╝  
██║  ██║███████╗██████╔╝██║  ██║██║╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                            

In questo caso consideriamo il file come txt, se fosse stato binario, prima di splittarlo dobbiamo usare la funzione:
decode("utf-8") --> in questo modo possiamo decodificare il testo binario.
"""

def controllaPrimo(numero):
    for i in range(2, numero):
        if (numero % i == 0):
            # il numero non è primo
            return 0
            break
    # se tutto il ciclo viene eseguito, il mio numero è primo 
    return 1


def contaPrimi(nomeFile):
    file = open(nomeFile, "r").read()
    arrayNumeri = file.split()
    arrayPrimi = []

    quantiSonoINumeriPrimi = 0
    risultato = 0
    for i in range(len(arrayNumeri)):
        risultato = controllaPrimo(int(arrayNumeri[i]))
        if (risultato == 1):
            print(f"Numero primo trovato: {arrayNumeri[i]}")
            quantiSonoINumeriPrimi += 1
            arrayPrimi.append(int(arrayNumeri[i]))

    print(arrayPrimi[0:3])



if __name__ == "__main__":
    nomeFile = input("Inserisci il nome del file: ")
    contaPrimi(nomeFile)
