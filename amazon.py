from bs4 import BeautifulSoup
import requests
import re

url = "https://www.amazon.com.br/hz/wishlist/ls/2T9KJKD2CTGOG/"
html = requests.get(url).content

soup = BeautifulSoup(html, features="html.parser")

prinks = soup.find_all("a", {"class" :"a-link-normal"}, partial=False)

preak = soup.find_all("span", {"class":"a-offscreen"})

prices = []
for price in preak:
    prices.append(re.sub('\W+',' ', price.getText()))

links = []
titles = []
for link in prinks:
    if(link["href"].startswith("/dp/")):
        links.append(link["href"][:14]) 
        titles.append(re.sub('\W+',' ', link.getText()))

# Remove Duplicates
clean = list(dict.fromkeys(links))

with open("tower_of_blabla.txt", "w", encoding="utf-8") as output:
        output.write(str(links) + "\n" + str(titles) + "\n" + str(prices) + "\n")


