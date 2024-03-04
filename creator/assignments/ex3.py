sloch = input().strip().split()

m = int(sloch[0])
n = int(sloch[1])

M = list()
for i in range(m):
    linha = list()
    for elemento in input().strip().split():
        linha.append(int(elemento))
    M.append(linha)

for j in range(n):
    media = 0
    for i in range(m):
        media += M[i][j]

    media = media/m
    soma = 0
    for i in range(m):
        if M[i][j] < media:
            soma += 1

    print(soma, end=" ")