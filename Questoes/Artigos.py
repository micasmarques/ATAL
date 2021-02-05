while True:
    avaliadores = int(input())
    if avaliadores == 0:
        break
    banca = []
    qtsArtigosPorAvaliador = 0
    for i in range(avaliadores):
        artigos = int(input())
        banca.append({
            'totalArtigos': 0,
            'maximo': artigos
        })
        qtsArtigosPorAvaliador += artigos
    banca = sorted(banca, key=lambda k: k['maximo'], reverse=True)
    numeroArtigos = int(input())
    if numeroArtigos > qtsArtigosPorAvaliador:
        print("Impossible")
        continue
    while numeroArtigos > 0:
        for j in banca:
            if j['totalArtigos'] + 1 <= j['maximo'] and numeroArtigos > 0:
                j['totalArtigos'] += 1
                numeroArtigos -= 1
    for k in banca:
        print(k['totalArtigos'])