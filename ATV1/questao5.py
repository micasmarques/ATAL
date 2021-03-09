def mediana(A, B, n):
    i, j, a, b = 0, 0, 0, 0
    count = 0
    while count < n + 1:
        count += 1
        if i == n:
            a = b
            b = B[0]
            break
        elif j == n:
            a = b
            b = A[0]
            break

        if A[i] <= B[j]:
            a = b
            b = A[i]
            i += 1
        else:
            a = b
            b = B[j]
            j += 1
    return (a + b) / 2


tamanho = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

print(int(mediana(A, B, tamanho)))
