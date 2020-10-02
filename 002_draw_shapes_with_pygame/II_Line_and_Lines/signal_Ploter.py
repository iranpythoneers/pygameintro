import pygame
from random import randint
from math import pi, sin
pygame.init()
screenX = 800
screenY = 800
SIZE = [screenX, screenY]
screen = pygame.display.set_mode(SIZE)

class signal:
    def __init__(self, f, m, color = [255] * 3):
        self.f     = f
        self.max   = m
        self.color = color
        self.n     = 0
        self.shift = 0
        self.data  = []
        self.nextPos()
        self.nextPos()
        
    def nextPos(self):
        f = self.f(self.n)
        self.data += [[self.n, f]]
        self.n    += 1
    
    def shiftIt(self):
        if self.shift > 0:
            shift = self.data.copy()
            for data in shift:
                data[0] -= self.shift
            print(shift)
            return shift[self.shift:]
        return self.data
    
    def checkShift(self):
        if self.data[-1][0] > self.max:
            self.shift += 1
    
    def plot(self, screen):
        screen.fill([0] * 3)
        self.nextPos()
        self.checkShift()
        pygame.draw.lines(screen, self.color, False, self.shiftIt())

def f(x, offset = screenY // 2):
    return 200 * sin(x * pi /36) + randint(-10, 10) + offset

sigFx = signal(f, screenX)
while True:
    sigFx.plot(screen)
    pygame.display.update()
    pygame.time.delay(50)