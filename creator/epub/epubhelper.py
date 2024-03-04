import os
from os.path import join

class EpubHelper():        
    def __init__(self) -> None:
        pass 

    XHTML_TEMPLATE = HTML = '''<?xml version="1.0" encoding="utf-8" standalone="no"?>
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>$$TITLE$$</title>
        <link href="../styles/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div id="$$SLUG$$">
        $$CONTENT$$
        </div>
    </body>
    </html>'''

    MIMETYPE_TEMPLATE = "application/epub+zip"

    def bootstrap(self):
        # Based on the boilerplate seen in https://github.com/javierarce/epub-boilerplate
        book_structure = ['META-INF', 'OEBPS', join('OEBPS', 'images'), join('OEBPS', 'styles'),join('OEBPS', 'text')]
        for struct in book_structure:
            os.makedirs(join("__book__", struct), exist_ok=True)

        key_files = ["mimetype", ]
        file_contents = [self.MIMETYPE_TEMPLATE]
        for file, content in key_files, file_contents:
            with open(file, "w", encoding="UTF-8") as f:
                f.write(content)