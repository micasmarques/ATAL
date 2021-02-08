controle = 1
while True:
    assinatura = input()
    if assinatura == '0':
        break
    numeros = input()
    if controle != 1:
        print()
    print("Instancia " + str(controle))
    if assinatura in numeros:
        print("verdadeira")
    else:
        print("falsa")
    controle += 1
