# https://docs.python.org/3/library/html.parser.html
from ebooklib import epub

# http://docs.sourcefabric.org/projects/ebooklib/en/latest/tutorial.html
from html.parser import HTMLParser

book = epub.EpubBook()

# These are required metadata 
book.set_identifier('sample123456')
book.set_title('Sample book')
book.set_language('pt-br')

book.add_author('Aleksandar Erkalovic')
book.add_metadata('DC', 'description', 'This is description for my book')

# Custom Metadata
book.add_metadata(None, 'meta', '', {'name': 'key', 'content': 'value'})


# Create a chapter and fill it with HTML
c1 = epub.EpubHtml(title='Introduction',
                   file_name='intro.xhtml',
                   lang='en')
c1.set_content(u'<html><body><h1>Introduction</h1><p>Introduction paragraph.</p></body></html>')

c2 = epub.EpubHtml(title='About this book',
                   file_name='about.xhtml')
c2.set_content('<h1>About this book</h1><p>This is a book.</p>')

# print(c1.get_content())


# Adds another type of file to the epub
style = 'body { font-family: Times, Times New Roman, serif; }'

nav_css = epub.EpubItem(uid="style_nav",
                        file_name="style/nav.css",
                        media_type="text/css",
                        content=style)

# Adds the chapters and items to the epub file
book.add_item(c1)
book.add_item(c2)
book.add_item(nav_css)

# How to create the table of contents (it is a tuple/list)
book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
              (
                # Sections are just tuple with two values. First one is title of the section and 2nd is tuple/list with subchapters.
                epub.Section('Languages'),
                (c1, c2)
              )
            )

# This is how the book will be structed 
book.spine = ['nav', c1, c2]

# Adds this shit 
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Salva o livro
epub.write_epub('test.epub', book)



# print(book.get_metadata('DC', 'title'))
# print(book.get_metadata('DC', 'identifier'))
# print(book.get_metadata('DC', 'creator'))
# print(book.get_metadata('OPF', 'cover'))

# kill all script and style elements
# for script in soup(["script"]):
#     script.extract()    # rip it out

# # get text
# text = soup.find("section").get_text()

# # Snippet:
# # If you want to save a tag, put in the whitelist
# whitelist = ['a','img']
# # Select which attributes you want to whitelist from the whitelisted tags
# attrs_whtlst = ['src', 'href']
# # Clean all attributes from tags
# for tag in data:
#     if tag.name not in whitelist:
#         tag.attrs = {}
#     else:
#         attrs = dict(tag.attrs)
#         for attr in attrs:
#             if attr not in attrs_whtlst:
#                 del tag.attrs[attr]
