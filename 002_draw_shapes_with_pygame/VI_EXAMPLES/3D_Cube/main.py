import pygame
from consts import *
from myObject import *

pygame.init()
screen = pygame.display.set_mode(SIZE)

cube = threeObject(CUBE, screen, GREEN)
cube.scale(200)
cube.move(900)

while True:
    screen.fill(BLACK)
    points = cube.getPoints()
    pygame.draw.polygon(screen, cube.color, points, 1)
    cube.rotate3DX(1)
    cube.rotate3DY(1)
    cube.rotate3DZ(1)
    for point in points:
        point = [int(x) for x in point]
        pygame.draw.circle(screen, RED, point, 5)
    
    pygame.display.update()
    pygame.time.delay(DELAY)