from bs4 import BeautifulSoup
from ebooklib import epub


with open("google.html", "r", encoding="utf-8") as reader:
    html = reader.read()

soup = BeautifulSoup(html, features="html.parser")

body = soup.find("body").decode_contents()
style = soup.find("style").decode_contents()

book = epub.EpubBook()


# These are required metadata 
book.set_identifier('1234567890')
book.set_title('Bakemonogatari Pt.1')
book.set_language('pt-br')

book.add_author('Nisioisin')
book.add_metadata('DC', 'description', 'This is Bakemonogatari.')

book.set_cover("Cover.jpg", open("MonsterCover.jpg", "rb").read())

# Create a chapter and fill it with HTML
c1 = epub.EpubHtml(title='Introduction',
                   file_name='intro.xhtml',
                   lang='pt-br')


c1.set_content(body)

css = epub.EpubItem(uid="style",
                        file_name="style/style.css",
                        media_type="text/css",
                        content=style)

c1.add_item(css)
book.add_item(c1)
book.add_item(css)


book.spine = ['nav', c1]


# Adds this shit 
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# print(c1.get_content())


# Salva o livro
epub.write_epub('test.epub', book)

# text = soup.get_text()

# # break into lines and remove leading and trailing space on each
# lines = (line.strip() for line in text.splitlines())
# # break multi-headlines into a line each
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # drop blank lines
# text = '\n'.join(chunk for chunk in chunks if chunk)

# with open("output.txt", "w", encoding="utf-8") as output:
#     output.write(text)

# parser.feed(text)

