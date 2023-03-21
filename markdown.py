import commonmark
import os
import ebooklib

def retrieve_mdfiles(path: str) -> list:
    fillets = []
    if os.path.isdir(path):
        exclude = set([".obsidian", ".git"])
        for root, dirs, files in os.walk(path, topdown=True):
            [dirs.remove(d) for d in list(dirs) if d in exclude]
            for name in files:
                fillets.append(os.path.join(root, name))
        
    mds = [file for file in fillets if file.endswith(".md")]
    return mds

path = "/home/breno/codes/writing"

for file in retrieve_mdfiles(path):
    with open(file, "r", encoding="utf-8") as f:
        data = f.read()
        print(data)
        data = commonmark.commonmark(data)
        
        # break







# parser = commonmark.Parser()
# ast = parser.parse("Hello *World*")

# renderer = commonmark.HtmlRenderer()
# html = renderer.render(ast)
# print(html) # <p>Hello <em>World</em><p/>

# # inspecting the abstract syntax tree
# json = commonmark.dumpJSON(ast)
# commonmark.dumpAST(ast) # pretty print generated AST structure