def indice_maior_elemento(lista, indice_atual=0, indice_maior=0):
    if indice_atual == len(lista):
        return indice_maior
    else:
        if lista[indice_atual] > lista[indice_maior]:
            return indice_maior_elemento(lista, indice_atual + 1, indice_atual)
        else:
            return indice_maior_elemento(lista, indice_atual + 1, indice_maior)

print(indice_maior_elemento([1, 5, 3, 9, 2]))