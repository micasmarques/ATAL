def maximo(vetor, esquerda, direita):
    if direita == esquerda:
        return vetor[esquerda]
    centro = (esquerda + direita) // 2
    a = maximo(vetor, esquerda, centro)
    b = maximo(vetor, centro + 1, direita)

    if a > b:
        return a
    return b

# Exemplo: {5, 6, 7, 8, 9};
# Exemplo: {1, 2, 3, 4, 5};
#                     (5)
#                    (0, 4)
#                 /           \
#             3  /             \ 5
#          (0, 2)               (3, 4)
#          /  \                 /   \
#        2/    \3             4/     \5
#    (0, 1)    (2, 2)      (3, 3)     (4, 4)
#       /        \
#     1/          \2
# (0, 0)          (1, 1)
