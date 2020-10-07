import pygame
from math import sin, pi

pygame.init()
SIZE   = [800, 800]
screen = pygame.display.set_mode(SIZE)

def mySignal(x):
    domain = 300
    offset = 400
    return domain * sin(x * pi / 36) + offset

class Plot:
    def __init__(self, signal, size, screen, color = [255] * 3):
        self.signal = signal
        self.size   = size
        self.data   = []
        self.plot   = []
        self.time   = 0
        self.shift  = 0.5
        self.count  = 0
        self.color  = color
        self.step   = 1
        self.nextPos()
        self.nextPos()
    
    def nextPos(self, shift = True):
        MAX = self.size[0]

        data  = [self.time]
        data += [self.signal(self.time)]
        self.data += [data.copy()]
        self.plot  = self.data.copy()

        if self.time > MAX and shift:
            temp = []
            for pos in self.plot:
                pos[0] -= self.shift
                if pos[0] >= 0:
                    temp += [pos]
            
            last = temp[0][0]
            for i in range(1, len(temp)):
                temp[i][0] = last + self.step
                last = temp[i][0]
            self.plot = temp.copy()
        
        self.time += self.step
    
    def shiftIt(self):
        '''
        This Shitty Impleantation is wrong
        '''
        if self.time > self.size[0]:
            for pos in self.plot:
                pos[0] -= self.shift

    def plotSignal(self):
        self.nextPos()
        pygame.draw.aalines(screen, self.color, False, self.plot)

sig = Plot(mySignal, SIZE, screen)
while True:
    screen.fill([0] * 3)
    sig.plotSignal()
    pygame.time.delay(1)
    pygame.display.update()


