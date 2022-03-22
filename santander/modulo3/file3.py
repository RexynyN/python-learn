import requests

url = "https://api.exchangerate-api.com/v6/latest"

req = requests.get(url)

print(req.status_code)

dados = req.json()

# print(dados)

valor = float(input("Informe o valor em reais a ser convertido para dolar"))

cotacao = dados['rates']['BRL']

print(f'R${valor} em dólar valem US$ {(valor / cotacao):.2f}')