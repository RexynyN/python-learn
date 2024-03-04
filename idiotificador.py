import random
import math

def charsplit(word):
    return [char for char in word]

frase = input("Idiotificador de frase, coloque a sua: ")
array = charsplit(frase)

for i in range(0, len(array)):
    rand = math.floor(random.randint(1,10))

    if((rand % 2) == 0):
        array[i] = array[i].upper()
    else:
        array[i] = array[i].lower()

frase = ''
print(frase.join(array))

