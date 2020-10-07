while True:
    try:
        entrada = [int(x) for x in input().split()]
        i = entrada[0]
        j = entrada[1]


        def solution(i, j):
            toRtn = 1
            for n in range(i, j + 1):
                count = 1
                while n != 1:
                    if n % 2 == 0:
                        n = n / 2
                    else:
                        n = (3 * n) + 1
                    count += 1
                toRtn = max(toRtn, count)
            return toRtn


        saida = solution(entrada[0], entrada[1])

        print(i, j, saida)
    except EOFError:
        break
