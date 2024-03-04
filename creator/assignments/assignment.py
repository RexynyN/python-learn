import math


# Exercicio 1 ============================================================
def function(x, b):
    return (2 * pow(x, 2)) + (b * x) - 2

def derivative(x, b):
    return 4 * x + b


def newton_raphson(b, iteracoes):
    iteracao = 0
    x1 = 0
    x0 = 0
    while iteracao < iteracoes or function(x1, b) != 0.0:
        x1 = x0 - (function(x0, b)/derivative(x0, b))
        x0 = x1
        iteracao += 1

    print("A raiz encontrada x =", x1)
    print()


# Exercicio 2 ============================================================
def tem_solucao(aux, new, e=1):
    for i, j in zip(aux, new):
        if (i + j)/2 > e:
            return False
    
    return True


def gauss_jacobi(A, b, vetor_solucao, iteracoes):
    iteracao = 0
    aux = []
    for i in range(len(vetor_solucao)):
        aux.append(0)

    while iteracao < iteracoes:
        vetor_aux = vetor_solucao.copy()

        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j] * vetor_solucao[j]
            x /= A[i][i]
            aux[i] = x
        iteracao += 1

        for p in range(len(aux)):
            vetor_solucao[p] = aux[p]

        solucao = tem_solucao(vetor_aux, vetor_solucao, 1)

    # print(vetor_solucao)
    if solucao:
        print("Tem solução!")
    else:
        print("Não tem solução!")
    print()
    

def gauss_seidel(A, b, vetor_solucao=[], iteracoes=10):
    iteracao = 0
    while iteracao < iteracoes:
        vetor_aux = vetor_solucao.copy()
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j] * vetor_solucao[j]
            x /= A[i][i]
            vetor_solucao[i] = x
        iteracao += 1

        solucao = tem_solucao(vetor_aux, vetor_solucao, 1)

    # print(vetor_solucao)
    if solucao:
        print("Tem solução!")
    else:
        print("Não tem solução!")
    print()
    


if __name__ == "__main__":
    # Exercicio 1 ============================================================
    b = -4
    iteracoes = 10
    newton_raphson(b, iteracoes)

    # Exercicio 2 Parte 1 ===================================================

    # B a ser usado nas iterações
    b = -3

    # Variaveis  
    A = [[3, b], [b, -3]]
    c = [1, 2]
    vetor_solucao = [0, 0]
    iteracoes = 30
    gauss_jacobi(A, c, vetor_solucao, iteracoes)

    # Exercicio 2 Parte 2 ===================================================
    gauss_seidel(A, c, vetor_solucao, iteracoes)
