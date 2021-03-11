def particao(lista, e, d):
    x = lista[d]
    i = e
    for j in range(e, d):
        if lista[j] <= x:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1

    lista[i], lista[d] = lista[d], lista[i]
    return i


def mediana(lista, e, d, k):
    if (k > 0 and k <= d - e + 1):
        index = particao(lista, e, d)

        if (index - e == k - 1):
            return lista[index]

        if (index - e > k - 1):
            return mediana(lista, e, index - 1, k)

        return mediana(lista, index + 1, d, k - index + e - 1)

    return INT_MAX

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
d = n - 1

tamanho = n

if n % 2 == 0:
  k = n / 2
else:
  k = (n + 1) / 2

print(menor, mediana(lista, 0, d, k), maior)
