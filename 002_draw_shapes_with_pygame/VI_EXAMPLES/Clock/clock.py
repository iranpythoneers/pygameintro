import time
import pygame
import jdatetime
from math import sin, cos, pi, radians

pygame.init()
X = Y  = 800
SIZE   = [X, Y]
screen = pygame.display.set_mode(SIZE)
BLACK  = [0] * 3

class Clock:
    def __init__(self, size, radius, screen, color = [255] * 3 ):
        self.screen = screen
        self.color  = color
        self.cx     = size[0] // 2 # Center X
        self.cy     = size[1] // 2 # Center Y
        self.radius = radius
        
        self.pivotH = [self.cx, self.cy - self.radius + self.radius / 2]
        self.pivotM = [self.cx, self.cy - self.radius + self.radius / 10]
        self.pivotS = [self.cx, self.cy - self.radius + self.radius / 30]

        self.endH   = None # End Hour
        self.endM   = None # End minute
        self.endS   = None # End Second
       
        self.setEndPoitns()

    def getTime(self):
        return jdatetime.datetime.now()
    
    def setEndPoitns(self):
        currentTime = self.getTime()
        
        hours  = currentTime.hour
        hours  = hours if hours < 13 else hours - 12
        minute = currentTime.minute
        second = currentTime.second

        thetaH = 360 * hours  / 12 # 12 -> Hourse
        thetaM = 360 * minute / 60 # 60 -> Minutes
        thetaS = 360 * second / 60 # 60 -> Seconds


        self.endH = self.rotate(self.pivotH, thetaH)
        self.endM = self.rotate(self.pivotM, thetaM)
        self.endS = self.rotate(self.pivotS, thetaS)
    
    def rotate(self, pos, degree):
        theta = radians(degree)
        sinT  = sin(theta)
        cosT  = cos(theta)
        px    = pos[0] - self.cx
        py    = pos[1] - self.cy
        newX  = px * cosT - py * sinT + self.cx
        newY  = py * cosT + px * sinT + self.cy
        return [newX, newY]
    
    def drawClock(self):
        scr  = self.screen
        clr  = self.color
        cntr = [self.cx, self.cy]
        r    = self.radius 
        # Draw Clock Circle
        pygame.draw.circle(scr, clr, cntr, r, 1)
        # Draw Hour Hand
        pygame.draw.line(scr, clr, cntr, self.endH)
        # Draw Minute Hand
        pygame.draw.line(scr, clr, cntr, self.endM)
        # Draw Hour Second
        pygame.draw.line(scr, clr, cntr, self.endS)
        # Update End Points
        self.setEndPoitns()

myColock = Clock(SIZE, 200, screen)

while True:
    screen.fill(BLACK)
    myColock.drawClock()
    pygame.time.delay(1)
    pygame.display.update()