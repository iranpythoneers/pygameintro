import pygame, math

def rotatePos(pos, degree, pivot = [0, 0]):
    theta = math.radians(degree)
    sinTheta = math.sin(theta)
    cosTheta = math.cos(theta)

    px = pos[0] - pivot[0]
    py = pos[1] - pivot[1]
    
    newX = px * cosTheta - py * sinTheta + pivot[0]
    newY = py * cosTheta + px * sinTheta + pivot[1]
    
    return [newX, newY]

pygame.init()
screenX = 800
screenY = 800
SIZE    = [screenX, screenY]
screen = pygame.display.set_mode(SIZE)

COLOR = [255] * 3
CLOSE = True

startPos    = [p // 2 for p in SIZE]
endPos      = [500, 500]
anotherPos  = [470, 610]

while True:
    screen.fill([0] * 3)
    #pygame.draw.line(screen, COLOR, startPos, endPos, 5)
    pygame.draw.lines(screen, COLOR, CLOSE, [startPos, endPos, anotherPos], 5)
    anotherPos = rotatePos(anotherPos, 10, startPos)
    endPos = rotatePos(endPos, 10, startPos)
    pygame.display.update()
    pygame.time.delay(30)