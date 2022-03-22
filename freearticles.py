
from bs4 import BeautifulSoup
import requests
  
# Website URL
url = 'https://super.abril.com.br/especiais/cesar-lattes-a-vida-e-a-obra-do-fisico-brasileiro-indicado-7-vezes-ao-nobel/'
  
# Page content from Website URL
page = requests.get(url).content
  
# parse html content
soup = BeautifulSoup(page, "html.parser")

# for data in soup(['style', 'script']):
for data in soup(['script']):
    # Remove tags
    data.decompose()

with open("flob.html", "w", encoding="utf-8") as f:
    f.write(soup.decode_contents())



  
