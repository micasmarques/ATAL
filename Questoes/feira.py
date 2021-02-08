# -*- coding: utf-8 -*-
idas = int(input())
for i in range(idas):
    produtos = int(input())
    dict_produco = {}
    for j in range(produtos):
        lista = input().split()
        dict_produco[lista[0]] = [float(lista[1])]
    compras = int(input())
    soma = 0.0
    for j in range(compras):
        lista = input().split()
        lista[1] = int(lista[1])
        if lista[0] in dict_produco.keys():
            var = dict_produco[lista[0]]
            soma += var[0]*lista[1]
    print("R$ %.2f" %soma)
