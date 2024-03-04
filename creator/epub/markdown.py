import shutil
import zipfile
import pathlib
import re
import unicodedata
import commonmark
import os
from bs4 import BeautifulSoup
from os.path import join, sep


def zip_epub(title: str, path: str = "__book__") -> None:
	directory = pathlib.Path(path)
	with zipfile.ZipFile(f"{title}.epub", mode="w") as zipf:
		for file in directory.rglob("*"):
			zipf.write(file, arcname=file.relative_to(directory))


def retrieve_mdfiles(path: str, recursive: bool = False, exclude_paths: str = []) -> list:
	fillets = []

	if not os.path.isdir(path):
		raise ValueError("Given path is not a directory")
	
	if recursive:
		exclude = set(exclude_paths)
		for root, dirs, files in os.walk(path, topdown=True):
			[dirs.remove(d) for d in list(dirs) if d in exclude]
			for name in files:
				fillets.append(os.path.join(root, name))
	else:
		fillets = [os.path.join(path, file) for file in os.listdir(path)]
		fillets = [file for file in fillets if not os.path.isdir(file)] 

	mds = [file for file in fillets if file.endswith(".md")]
	return mds

def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)


HTML = '''<?xml version="1.0" encoding="utf-8" standalone="no"?>
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

path = "/home/breno/codes/writing"

content_path = join('__book__', 'OEBPS', 'text')
for file in retrieve_mdfiles(path):
	print(file)
        
	with open(file, "r", encoding="utf-8") as f:
		data = f.read()
		data = commonmark.commonmark(data)
		# Get the name of the file
		title = file.split(sep)[-1].split(".")[0]
		content = HTML.replace("$$CONTENT$$", data)
		content = content.replace("$$TITLE$$", title)
		content = content.replace("$$SLUG$$", slugify(title))
		with open(join(content_path, f"{slugify(title)}.xhtml"), "w", encoding="UTF-8") as f:
			f.write(content)


zip_epub("TesteBreno", "__book__")
shutil.rmtree("__book__")






# parser = commonmark.Parser()
# ast = parser.parse("Hello *World*")

# renderer = commonmark.HtmlRenderer()
# html = renderer.render(ast)
# print(html) # <p>Hello <em>World</em><p/>

# # inspecting the abstract syntax tree
# json = commonmark.dumpJSON(ast)
# commonmark.dumpAST(ast) # pretty print generated AST structure