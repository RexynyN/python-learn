from sys import argv
import os

def get_dirfiles(path: str, filter = None, exclude: list = []) -> list:
    fillets = []
    if os.path.isdir(path):
        exclude = set(exclude)
        for root, dirs, files in os.walk(path, topdown=True):
            [dirs.remove(d) for d in list(dirs) if d in exclude]
            for name in files:
                fillets.append(os.path.join(root, name))
    if filter: 
        mds = [file for file in fillets if filter(file)]
    return mds

def find_numbered_dup(file, blobs):
    numbered = []
    for fillet in blobs:
        # Sees if it has the (1) at the end of the file and if the filename is there
        if file in fillet:
            aux = fillet.split("(")[-1]
            i = aux.find(")")
            if aux[:i].isdigit():
                numbered.append(fillet)
    
    return numbered



def find_dup(file, blobs):
    dups = []
    unique = True 
    for fillet in blobs:
        if fillet == file:
            dups.append(fillet)

    return dups

# MAIN PROGRAM

def main(argv):
    blobs = get_dirfiles(argv[-1])

    for file in blobs:
        find_dup()

if __name__ == "__main__":
    main(argv)