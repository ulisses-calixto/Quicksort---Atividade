def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        n_esquerda = []      
        n_direita = []
        for i in lista:
            if i != lista[0] and i <= pivo:
                n_esquerda.append(i)
        for i in lista:
            if i != lista[0] and i > pivo:
                n_direita.append(i)
        return quicksort(n_esquerda) + [pivo] + quicksort(n_direita)
numeros_d = [54, 26, 93, 17, 77, 31, 44, 55, 20]
resultado = quicksort(numeros_d)
print(resultado)  


