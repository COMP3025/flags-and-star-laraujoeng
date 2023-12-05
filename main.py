import pygame
import util
from math import pi

run = True
pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen.fill(util.gray)
pygame.display.set_caption("Atividade 01 - Flags")

# Brasil
pygame.draw.rect(screen, util.green, (0, 0, 500, 300), 0)
pygame.draw.polygon(screen, util.yellow, ((480, 150), (250, 50), (20, 150), (250, 250)))  # direita cima esquerda baixo
pygame.draw.circle(screen, util.blue, (250, 150), 70, 0)
pygame.draw.polygon(screen, util.white, ((320, 150), (180, 140), (180, 150), (318, 160)))  # direita cima esquerda baixo
pygame.draw.rect(screen, util.red, (600, 0, 500, 120), 0)
pygame.draw.rect(screen, util.blue, (600, 181, 500, 120), 0)
pygame.draw.polygon(screen, util.yellow, ((600, 0), (600, 300), (900, 150)), 0)

# Áfrifa do sul
pygame.draw.line(screen, util.white, (850, 150), (1099, 150), 120)
pygame.draw.polygon(screen, util.black, ((600, 40), (600, 260), (750, 150)), 0)
pygame.draw.polygon(screen, util.white, ((950, 150), (750, 0), (700, 0), (800, 150)))  # direita cima esquerda baixo
pygame.draw.polygon(screen, util.white, ((950, 150), (750, 300), (700, 300), (850, 150)))  # direita cima esquerda baixo
pygame.draw.line(screen, util.green, (850, 150), (1099, 150), 65)
pygame.draw.polygon(screen, util.green, ((900, 150), (700, 0), (600, 0), (800, 150)))  # direita cima esquerda baixo
pygame.draw.polygon(screen, util.green, ((900, 150), (700, 300), (600, 300), (800, 150)))  # direita cima esquerda baixo

# Brasil
pygame.draw.rect(screen, util.white, (0, 400, 500, 300), 0)
pygame.draw.rect(screen, util.green, (0, 400, 250, 300), 0)

pygame.draw.circle(screen, util.red, (250, 550), 100, 0)

pygame.draw.circle(screen, util.white, (280, 550), 80, 0)
pygame.draw.arc(screen, util.green, [200, 478, 100, 145], pi / 2, 3 * pi / 2, 50)

a = 14
b = 180
c = 84
d = 277
e = 38
f = 40 * -1
g = 60 * -1
h = 252 * -1
i = 76 * -1
j = 115 * -1

pygame.draw.polygon(screen, util.red, [(165, 151), (200, 20), (235, 151), (371, 144), (257, 219),
                                       (306, 346), (200, 260), (94, 346), (143, 219), (29, 135)], 0)

pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
