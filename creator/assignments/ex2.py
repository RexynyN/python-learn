from math import floor

n = int(input())

if n == 1:
    print(f"X = {input()}")
    exit()

M = list()
for i in range(n):
    linha = list()
    for elemento in input().strip().split():
        linha.append(int(elemento))
    M.append(linha)

soma = 0
for i, j in zip(range(n), reversed(range(n))):
    soma += M[i][j]

for i in range(n):
    soma += M[i][i]

# Tem que tirar o elemento no "meio" do X, porque ele e contabilizado duas vezes
soma -= M[floor(n/2)][floor(n/2)]

print(soma)
