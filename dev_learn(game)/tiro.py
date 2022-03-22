import pygame

class Shot(object):
    tir = {
        "x": 0,
        "y": 0,
        "color": (0, 255, 0)
    }

    def __init__(self, x, y):
        self.tir["x"] = x
        self.tir["y"] = y

    def shoot(self, display):
        while self.tir["x"] < 4000:
            tiro = pygame.Rect(self.tir["x"] + 20, self.tir["y"] + 20, 10, 10)
            pygame.draw.rect(display, self.tir["color"], tiro)
            self.tir["x"] += 1
