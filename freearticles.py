
from bs4 import BeautifulSoup
import requests
  
# Website URL
url = 'https://newsletters.theatlantic.com/i-have-notes/636fe36008bfc30037f51c9d/creative-writing-schedule-routine-pitching-tips/'
  
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



  
