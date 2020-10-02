import pygame

pygame.init()

screenX = 800
screenY = 800
SIZE = [screenX, screenY]
screen = pygame.display.set_mode(SIZE)

startPos = [400, 400]
endPos   = [500, 550]

while True:
    pygame.draw.aaline(screen, [255] * 3, startPos, endPos)
    pygame.display.update()
    pygame.time.delay(200)