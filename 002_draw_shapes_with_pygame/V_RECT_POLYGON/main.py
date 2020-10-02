import pygame
from math import sin, cos, pi
pygame.init()

def regularPolygon(x, y, n = 3, r = 50):
    for i in range(n):
        theta = 2 * pi * i / n
        yield [r * cos(theta) + x, r * sin(theta) + y]
        

X = Y = 800
SIZE    = [X, Y]
screen  = pygame.display.set_mode(SIZE)
WHITE   = [255] * 3
BLACK   = [0] * 3
color   = WHITE
width   = 1

startX  = 400
startY  = 400
lentghX = 250
lentghY = 150

rect = [startX, startY, lentghX, lentghY]
rect = pygame.Rect(rect)
n = 3
while True:
    screen.fill(BLACK)
    points = list(regularPolygon(400, 400, n, 200))
    #pygame.draw.rect(screen, color, rect, width)
    pygame.draw.polygon(screen, WHITE, points, width)
    n += 1
    pygame.time.delay(10)
    pygame.display.update()