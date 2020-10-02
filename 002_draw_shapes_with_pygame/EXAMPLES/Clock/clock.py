import time
import pygame
import jdatetime

pygame.init()
X = Y  = 800
SIZE   = [X, Y]
screen = pygame.display.set_mode(SIZE)

class Clock:
    def __init__(self, size, radius):
        self.cx     = size[0] // 2
        self.cy     = size[1] // 2
        self.radius = radius
        self.pivotH = self.cy + self.radius - self.radius * 3 / 10
        self.pivotM = self.cy + self.radius - self.radius * 2 / 10
        self.pivotS = self.cy + self.radius - self.radius / 10
        self.endH   = self.pivotH
        self.endM   = self.pivotM
        self.endS   = self.pivotS

    def getTime(self):
        return jdatetime.time.now()
    
    def setEndPoitns(self):
        currentTime = self.getTime()
        thetaM = None
        thetaH = None
        thetaS = None