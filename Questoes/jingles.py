notas = {
    "W":1/1,
    "H":1/2,
    "Q":1/4,
    "E":1/8,
    "S":1/16,
    "T":1/32,
    "X":1/64
}
while True:
    composicao = input()
    if composicao == "*":
        break
    musica = composicao.strip("/").split("/")
    tempo = 0
    for i in musica:
        controle = 0
        for j in i:
            controle += notas[j]
        if controle == 1:
            tempo += 1
    print(tempo)