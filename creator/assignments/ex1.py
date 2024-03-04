n = int(input())

M = list()
for i in range(n):
    linha = list()
    for elemento in input().strip().split():
        linha.append(int(elemento))
    M.append(linha)

menor = M[0][0]
for i, j in zip(range(n), reversed(range(n))):
    if M[i][j] < menor:
        menor = M[i][j]

index = 0
for i in range(n):
    if M[index][i] < menor:
        menor = M[index][i]

index = n - 1
for i in range(n):
    if M[index][i] < menor:
        menor = M[index][i]

print(menor)
