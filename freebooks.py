from genericpath import isdir
from urllib.request import urlopen
from bs4 import BeautifulSoup
from ebooklib import epub
import requests
import shutil
import os
import json
import re

def handleInput(filename):
    try:
        with open(filename, "r") as read_file:
            data = json.load(read_file)
    except:
        print("O arquivo de configuração não foi encontrado, ou não está na formatação correta.")
    return data

    
# Uses the img source to download the image
def handleImg(src):
    img_path = os.getcwd() + "\\__img_data__\\"

    if(not os.path.isdir(img_path)):
        os.mkdir(img_path)

    dir = os.listdir(img_path)

    image_url = src
    filename = image_url.split("?")[0].split("/")[-1]

    if not filename in dir:
        print("Baixei " + filename)
        r = requests.get(image_url, stream=True)
        r.raw.decode_content = True

        with open(img_path + filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return filename


def scrapBook(sett):
    content = {"files": [], "images": []}
    # Here we gathe the chapter and images from the site
    for vars in sett['variacao']:
        file = {}

        url = sett['url'].replace("*", vars)
        # html = requests.get("https://tsundokutraducoes.com.br/projetos/mushoku-tensei-reencarnacao-do-desempregado/vol-01/cap-07/").content
        with open(url, "r", encoding="utf-8") as read_file:
            html = read_file.read()

        soup = BeautifulSoup(html, features="html.parser")

        # Possíveis soluções para as querys

        # Pegar a primeira frase do texto, e pegar o parent node
        # for img in soup.find_all('img'):
        #     if img.parent.name == 'a':
        #         print ("Parent is a link")

        # Pegar a hierarquia de divs e procurar pelos childrens
        # li = soup.find('li', {'class': 'text'})
        # for child in li.children:
        #     print(child)        



        blacklist = ['''<p class=""><em><strong>📃 Outras Informações 📃</strong></em></p>
<p class=""> </p>
<p class=""><strong>Apoie a scan para que ela continue lançando conteúdo, comente, divulgue, acesse e leia as obras diretamente em nosso site.</strong></p>
<p class=""> </p>
<p class=""><strong>Que tal ver a <del>calcinh…</del> cof cof, a Roxy em forma de mangá?! cliquem na imagem e sejam felizes</strong> <img src="images/703106689649606657.gif"/></p>
<p class=""> </p>
<p class=""><a href="https://www.animexnovel.com/2019/07/mushoku-tensei-roxy-manga.html"><img src="images/Roxy.png"/></a>  <strong>Quer dar uma forcinha para o site? Que tal acessar nosso Padrim <img src="images/615958021746720769.png"/></strong></p>
<p class=""><strong><a href="https://www.padrim.com.br/tsundoku" rel="noopener noreferrer" target="_blank"><img src="images/Padrim.png"/></a></strong></p>
<p class=""><strong>Acessem nosso Discord, receberemos vocês de braços abertos.<img src="images/751870123995824201.png"/></strong></p>
<p class=""> </p>
<p class=""><a href="https://discord.com/invite/GMVgjpA" rel="noopener noreferrer" target="_blank"><img src="images/Discord-LogoWordmark-Color.png"/></a></p>
<p class=""> </p>''']

        stringSoup = str(soup).strip()
        for string in blacklist:
            stringSoup = stringSoup.replace(string, "")

        soup = BeautifulSoup(stringSoup, features="html.parser")

        # Queries
        if(soup.find_all("div", {"id": "target-id61638384ba04f"})):
            data = soup.find_all("div", {"id": "target-id61638384ba04f"})[0]
        elif(soup.find_all("div", {"style": "text-indent: 30px; text-align: justify;"})):
            data = soup.find_all(
                "div", {"style": "text-indent: 30px; text-align: justify;"})[0]
        elif(soup.find_all("div", {"class": "text-left"})):
            data = soup.find_all("div", {"class": "text-left"})[0]
        elif(soup.find_all("div", {"style": "text-indent: 30px;"})[0]):
            data = soup.find_all("div", {"style": "text-indent: 30px;"})[0]
        else:
            data = soup.find_all("div", {"style": "text-indent: 30px;"})[1]

        cap_title = soup.find("li", {"class": "active"})

        file['capitulo'] = cap_title.get_text().strip()

        cssClass = ""
        # Sanitizes all paragraphs, putting the same class to everyone
        for tag in data.find_all('p'):
            tag.attrs = {}
            tag['class'] = cssClass

        # Finds all images and downloads
        for tag in data.find_all("img"):
            src = handleImg(tag['src'])
            tag.attrs = {}
            tag['src'] = "images/" + src
            content['images'].append(src)

        # gets the text
        text = data.decode_contents()

        

        # To replace the HTML
        # cleanSoup = BeautifulSoup(str(originalSoup).replace("<br/>", replaceString))

        # text = text.replace(replace, "")

        cap = file['capitulo']
        text = f'<h3>{cap}</h3> {text}'

        # Leaves the Text Prettier
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip()
                  for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        file['texto'] = text
        content['files'].append(file)

    return content


def defaultStyle():
    return '''
            @namespace epub "http://www.idpf.org/2007/ops";
            body {
                font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
            }
            h2 {
                text-align: left;
                text-transform: uppercase;
                font-weight: 200;     
            }
            ol {
                    list-style-type: none;
            }
            ol > li:first-child {
                    margin-top: 0.3em;
            }
            nav[epub|type~='toc'] > ol > li > ol  {
                list-style-type:square;
            }
            nav[epub|type~='toc'] > ol > li > ol > li {
                    margin-top: 0.3em;
            }
            body { 
                font-family: Times, 
                Times New Roman, serif; 
            }
        '''


def createBook(data, sett):
    # Inicializing the ebook
    book = epub.EpubBook()

    book.set_identifier(sett["id"])
    book.set_title(sett['titulo'])
    book.set_language(sett['lingua'])

    book.add_author(sett['autor'])
    book.add_metadata('DC', 'description', sett['descricao'])

    book.set_cover("cover.png", open(sett['capa'], 'rb').read())

    if(sett['estilo'] == "default" or sett['estilo'] == "" or sett['estilo'] == " "):
        style = defaultStyle()
    else:
        with open(sett['estilo'], "r") as read_file:
            style = read_file.read()

    css = epub.EpubItem(uid="style_nav",
                            file_name="style/style.css",
                            media_type="text/css",
                            content=style)

    spine = ["cover", "nav"]
    for file in data['files']:
        # Create a chapter and fill it with HTML and css
        c = epub.EpubHtml(title=file['capitulo'],
                          file_name=file['capitulo'] + '.xhtml',
                          lang=sett['lingua'])
                          
        c.set_content(file['texto'])
        c.add_item(css)
        book.add_item(c)
        spine.append(c)


    data["images"] = list(set(data['images']))
    for img in data['images']:
        p = epub.EpubItem(file_name=f"images/{img}", content=open('__img_data__\\' +
                          img, 'rb').read(), media_type='image/' + img.split(".")[-1])
        book.add_item(p)

    # p1 = epub.EpubItem(file_name='images/artefatoDivino.png', content=open('__img_data__\\artefatoDivino.png', 'rb').read(), media_type='image/png')
    # p2 = epub.EpubItem(file_name='images/Imagem_MT_07.png', content=open('__img_data__\\Imagem_MT_07.png', 'rb').read(), media_type='image/png')
    # book.add_item(p1)
    # book.add_item(p2)

    # How to create the table of contents (it is a tuple/list)
    # book.toc = ((epub.Section("Capítulos"), (c1)))

    # This is how the book will be structed
    book.spine = spine

    # Adds this shit
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.add_item(css)

    # Salva o livro
    epub.write_epub(sett['titulo'] + '.epub', book)

    # with open("output.txt", "w", encoding="utf-8") as output:
    #     output.write(text)


def main():
    settings = handleInput("input.json")
    data = scrapBook(settings)
    createBook(data, settings)


if __name__ == '__main__':
    main()
