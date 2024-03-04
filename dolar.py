import requests 

# Lets get the fucking Dolar Price For Tourism
url = "https://economia.awesomeapi.com.br/all/USD-BRLT"

# url = "https://cep.awesomeapi.com.br/json/02073070"

response = requests.get(url)

# print(response.json())

if response.status_code == 200:
    valor_dolar = response.json()["USDT"]["low"]
    print(f"O valor do Dólar é R${valor_dolar}")
else:
    print("Erro de buscar na API")