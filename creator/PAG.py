from time import sleep as sleep 
import pyautogui as pag
from math import floor

class PAG:
    def __init__ (self, x_div=1, y_div=1):
        self.width, self.height= pag.size()
        self.x_div = x_div
        self.y_div = y_div
        self.x_part = floor(self.width / x_div)
        self.y_part = floor(self.height / y_div)

    def click_middle(self, x_sector, y_sector, button="left"):
        if x_sector > self.x_div or x_sector <= 0:
            print("Invalid X-Axis Sector")

        if y_sector > self.y_div or y_sector <= 0:
            print("Invalid Y-Axis Sector")


        pag.click(x=910, y=500, button=button)
