import pygame


class Player(object):
    ret = {
        "x": 0,
        "y": 0,
        "size": [50, 50],
        "color": (0, 0, 255)
    }

    tir = {
        "x": 0,
        "y": 0,
        "color": (0, 255, 0)
    }

    def __init__(self):
        self.resolution = {
            "x": pygame.display.get_window_size()[0],
            "y": pygame.display.get_window_size()[1]
        }

    def gameplay(self, display):
        # configurações do retângulo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.ret["x"] >= 0 and self.ret["x"] <= (self.resolution["x"] - 50):
                self.ret["x"] += 0.5
            else:
                if self.ret["x"] <= 0:
                    self.ret["x"] = 0
                else:
                    self.ret["x"] = (self.resolution["x"] - 50)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.ret["x"] >= 0 and self.ret["x"] <= (self.resolution["x"] - 50):
                self.ret["x"] -= 0.5
            else:
                if self.ret["x"] < 0:
                    self.ret["x"] = 0
                else:
                    self.ret["x"] = self.resolution["x"] - 50

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.ret["y"] >= 0 and self.ret["y"] <= (self.resolution["y"] - 50):
                self.ret["y"] -= 0.5
            else:
                if self.ret["y"] < 0:
                    self.ret["y"] = 0
                else:
                    self.ret["y"] = self.resolution["y"] - 50

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.ret["y"] >= 0 and self.ret["y"] <= (self.resolution["y"] - 50):
                self.ret["y"] += 0.5
            else:
                if self.ret["y"] < 0:
                    self.ret["y"] = 0
                else:
                    self.ret["y"] = self.resolution["y"] - 50

        if keys[pygame.K_SPACE] or keys[pygame.K_k]:
            self.tir["x"] = self.ret["x"]
            self.tir["y"] = self.ret["y"]
            self.shoot(display)

        retangulo = pygame.Rect(self.ret["x"], self.ret["y"], 50, 50)
        pygame.draw.rect(display, self.ret["color"], retangulo)

    def shoot(self, display):
        tiro = pygame.Rect(self.tir["x"] + 20, self.tir["y"] + 20, 10, 10)
        pygame.draw.rect(display, self.tir["color"], tiro)
        self.tir["x"] += 0.1
