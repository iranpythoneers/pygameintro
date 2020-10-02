#!/usr/bin/python3.8
import pygame
import math
pygame.init()
X = 800
Y = 600
SIZE = [X, Y]
screen = pygame.display.set_mode(SIZE)
radius = 10
sign   = 1
RECT   = pygame.Rect(X // 2 - 100, Y // 2 - 100, 200, 200)
 
def drawMyCircle(const = 10, color = [255] * 3, width = 1, limit = 250):
    global screen, SIZE, radius, sign
    center = [x // 2 for x in SIZE]
    pygame.draw.circle(screen, color, center, radius, width)
    if radius > limit:
        sign = -1
    elif radius < const + width + 1:
        sign = 1
    radius += sign * const
    
def drawEllipse(sx, sy, lx, ly, color = [255] * 3, width = 1):
    global screen
    rect = pygame.Rect(sx, sy, lx, ly)
    pygame.draw.ellipse(screen, color, rect, width)

def drawArc(start, end, rect = RECT, color = [255] * 3, width = 1):
    global screen
    start = math.radians(start)
    end   = math.radians(end)
    pygame.draw.arc(screen, color, rect, start, end, width)

angle = 1
ellipse = pygame.Rect(200, 250, 128, 256)
while True:
    screen.fill([0] * 3)
    # drawMyCircle()
    # drawEllipse(100, 100, 165, 165)
    drawArc(0, angle, ellipse)
    angle += 1
    angle %= 361
    pygame.time.delay(10)
    pygame.display.update()