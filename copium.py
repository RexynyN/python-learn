from bs4 import BeautifulSoup
from pathlib import Path
import requests
from json import loads as json_loads

i = 0
i = int(i)
link = [0]
# link[0]=input()
link[0] = "https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Neon%20Revolution%20%28Field-Tested%29"

for x in link:  # salva o source em um txt
    html = requests.get(link[i]).content
    soup = BeautifulSoup(html, 'html.parser')
    penis = soup.prettify()
    arquivo = open('source.txt', 'a', encoding="utf-8")
    arquivo.write(penis+"\n")
    arquivo.close()
    i += 1

with open('source.txt', 'rb') as file_in:  # abre o source e salva um txt com todos os json
    with open("output.txt", "wb") as file_out:
        file_out.writelines(
            filter(lambda line: b'var g_rgAssets =' in line, file_in))


with open('output.txt', encoding="utf-8") as f:  # converte pra json
    contents = f.read()


b = contents.replace("var g_rgAssets =", " ")
b = b.replace(
    "border: 2px solid rgb(102, 102, 102); border-radius: 6px; width=100; margin:4px; padding:8px;", " ")
b = b.replace("\t", "")
b = b.replace("\n", "")
b = b.replace(" ", "")

jsons = b.split(";")

weapon_ids = []
for json in jsons:
    try:
        p = json_loads(json)
    except Exception:
        continue

    aux = p['730']['2']

    for key, value in aux.items():
        link = aux[key]["actions"][0]["link"]
        weapon_ids.append(link.replace("%assetid%", key))


with open("links.txt", "w", encoding="utf-8") as f:
    for id in weapon_ids:
        f.write(f"{id}\n")
    

