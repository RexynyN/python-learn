import pygame
import math
from player import Player

pygame.init()

screen_size = (900, 900)

display = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Nome do Jogo")

# configurações do retângulo
ini = {
    "x": 0,
    "y": 0,
    "size": [50, 50],
    "color": (255, 0, 0)
}

cont = 0

resolution = {
    "x": pygame.display.get_window_size()[0],
    "y": pygame.display.get_window_size()[1]
}

background = pygame.image.load("./Bakemonogatari wallpaper.jpg")
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill((0, 0, 0))
    display.blit(background, (0, 0))

    player.gameplay(display)

    ini["x"] = cont
    ini["y"] = cont

    # circulo = pygame.draw.circle(display, color, ret_pos, 50)
    # retangulo = pygame.Rect(ret["x"], ret["y"], 50, 50)
    inimigo = pygame.Rect(ini["x"], ini["y"], 50, 50)
    # pygame.draw.rect(display, ret["color"], retangulo)
    pygame.draw.rect(display, ini["color"], inimigo)
    pygame.display.update()

    cont += 0.2