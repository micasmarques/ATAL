def verifica_col(col, item, base_minima):
    if col < len(item):
        return base_minima
    else:
        return 0


def countingSort(lista, tamanho_lista, col):
    saida = [0] * tamanho_lista
    contador = [0] * (26 + 1)
    base_minima = ord('a') - 1

    for i in lista:
        letra = ord(i[col]) - verifica_col(col, i, base_minima)
        contador[letra] += 1

    for i in range(len(contador) - 1):
        contador[i + 1] += contador[i]

    for i in reversed(lista):
        letra = ord(i[col]) - verifica_col(col, i, base_minima)
        saida[contador[letra] - 1] = i
        contador[letra] -= 1

    return saida


def radixSort(array):
    for i in range(5 - 1, -1, -1):
        array = countingSort(array, len(array), i)
    return array


lista = ["abcde", 'abcaa', 'abbbb', 'abaaa', 'aaaaa']
print(radixSort(lista))
