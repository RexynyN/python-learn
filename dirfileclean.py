import os
import re
from os.path import join

# Returns if a file a is numbered duplicate similar as in: image(1).jpeg
def is_numbered_duplicate(filename: str):
    # Finds last occurance of the parenthesis, as it could have many occurances
    idx = filename.rfind("(")
    # Finds if the substring inside the parenthesis is a number
    result = re.search('\((.*?)\)', filename[idx:]).group()
    return result[1:-1].isnumeric()

# Find the twin (or original) file of a numbered duplicate
def numbered_duplicate_twin(path: str, duplicate: str):
    # Remove the numbered part of the file name
    split = duplicate.split(".")
    idx = split[0].rfind("(")
    split[0] = split[0][:idx].strip()
    clean_filename = ''.join([x + "." for x in split]).strip(".")

    # Return the twin filename (if it exists)
    twin = None
    for file in os.listdir(path):
        if file == clean_filename:
            twin = file
            break
    return join(path, twin)

print(numbered_duplicate_twin(".", "(breno))(( sexo (3).tar.gz"))