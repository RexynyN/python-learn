class Conta: 
    _descricao = "Cont"
    _valor = 0.0

    def __init__(self, desc, valor):
        self._valor = valor
        self._descricao = desc

    def parcelas(self, nParcelas):
        return self._valor/nParcelas

    def __str__(self):
        return (f"Noma da Conta: {self._descricao}, Valor: {self._valor}")


contaTeste = Conta("Uma conta teste", 10.0)


print(contaTeste)