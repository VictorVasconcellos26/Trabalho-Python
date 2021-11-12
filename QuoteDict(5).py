frase = input("Digite sua Frase: ")

def contarPalavras(frase):
    arrayDeTuplas = []
    arrayDePalavras = frase.upper().split(" ")
    conjuntoDePalavras = set(arrayDePalavras)
    for palavra in conjuntoDePalavras:
        quantidade = arrayDePalavras.count(palavra)
        arrayDeTuplas.append((palavra, quantidade))
    return dict(arrayDeTuplas)

print(contarPalavras(frase))



