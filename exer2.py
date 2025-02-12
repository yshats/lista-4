def soma_lista_aninhada(lista):
    soma = 0
    for elemento in lista:
        if isinstance(elemento, list):
            soma += soma_lista_aninhada(elemento)
        else:
            soma += elemento
    return soma

print(soma_lista_aninhada([1, [2, 3], [4, [5]]]))