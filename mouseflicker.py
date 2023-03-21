import pyautogui as pag
import random 

(width, height) = pag.size()

while True:
    randw = random.randint(0, width)
    randh = random.randint(0, height)

    pag.moveTo(randw, randh, 3.5)
