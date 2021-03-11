def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def median(arr, e, d, k):
    if 0 < k <= d - e + 1:
        index = partition(arr, e, d)

        if index - e == k - 1:
            return arr[index]

        if index - e > k - 1:
            return median(arr, e, index - 1, k)
        return median(arr, index + 1, d, k - index + e - 1)

    return 9999999999999


n = int(input())
maior = -1
menor = float('inf')
lista = []
for i in range(n):
    entrada = int(input())
    lista.append(entrada)
    if entrada > maior:
        maior = entrada
    if entrada < menor:
        menor = entrada

if n % 2 == 0:
    k = n / 2
else:
    k = (n + 1) / 2

print(menor, median(lista, 0, n - 1, k), maior)
